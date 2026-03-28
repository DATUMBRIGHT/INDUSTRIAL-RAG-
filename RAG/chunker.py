import gc
import os
from pathlib import Path
from typing import List

from llama_index.core.extractors import SummaryExtractor, TitleExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core import Document, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
import dotenv

dotenv.load_dotenv()

base_path = Path(__file__).parent.parent / "model"

if base_path.exists():
    print(f"base_path: {base_path}")
else:
    print("base_path not found. Please check the path to your model directory.")

BATCH_SIZE = 1
PERSIST_DIR = Path(__file__).parent.parent / "storage"

# Hard wrap any single line exceeding this char count before splitting.
# ~1500 chars ≈ 375 tokens — ensures no individual "sentence" blows embed context.
MAX_LINE_CHARS = 1500


def _preprocess_text(text: str) -> str:
    """Break oversized lines/blocks before the splitter sees them."""
    lines = text.split("\n")
    result = []
    for line in lines:
        if len(line) > MAX_LINE_CHARS:
            chunks = [line[i:i + MAX_LINE_CHARS] for i in range(0, len(line), MAX_LINE_CHARS)]
            result.extend(chunks)
        else:
            result.append(line)
    return "\n".join(result)


class DocChunker:
    def __init__(self, folder_path: Path = None):
        self.folder_path = folder_path

        self.embed_model = OllamaEmbedding(
            model_name="nomic-embed-text",
            base_url=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            embed_batch_size=16,
        )

        self.llm = Ollama(
            model="qwen3.5:35b-a3b",
            base_url=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            temperature=0.1,
            request_timeout=120.0,
        )

    def _iter_files(self):
        """Yield Documents one at a time — no bulk load into RAM."""
        for file in self.folder_path.glob("*.md"):
            with open(file, "r", encoding="utf-8") as f:
                yield Document(
                    text=_preprocess_text(f.read()),
                    doc_id=file.stem,
                    metadata={"file_name": file.name},
                )

    def embed_docs(self) -> VectorStoreIndex:
        """Chunk, extract metadata, embed and store locally — in batches."""
        if not self.folder_path:
            print("No folder path provided.")
            return None

        # Load existing index from disk if available
        if PERSIST_DIR.exists():
            print(f"Loading existing index from {PERSIST_DIR}")
            storage_context = StorageContext.from_defaults(persist_dir=str(PERSIST_DIR))
            return load_index_from_storage(storage_context, embed_model=self.embed_model)

        parser = SentenceSplitter(
            chunk_size=512,
            chunk_overlap=50,
            paragraph_separator="\n\n",
        )

        index = VectorStoreIndex([], embed_model=self.embed_model)

        pipeline = IngestionPipeline(
            transformations=[
                TitleExtractor(llm=self.llm),
                SummaryExtractor(summaries=["self"], llm=self.llm),
                self.embed_model,
            ],
        )

        batch: List[Document] = []
        for doc in self._iter_files():
            batch.append(doc)
            if len(batch) < BATCH_SIZE:
                continue
            self._process_batch(batch, parser, pipeline, index)
            batch = []

        if batch:
            self._process_batch(batch, parser, pipeline, index)

        PERSIST_DIR.mkdir(parents=True, exist_ok=True)
        index.storage_context.persist(persist_dir=str(PERSIST_DIR))
        print(f"Index persisted to {PERSIST_DIR}")

        return index

    def _process_batch(
        self,
        docs: List[Document],
        parser: SentenceSplitter,
        pipeline: IngestionPipeline,
        index: VectorStoreIndex,
    ) -> None:
        names = [d.metadata["file_name"] for d in docs]
        print(f"  Batch: {names}")

        nodes = parser.get_nodes_from_documents(docs, show_progress=False)
        processed_nodes = pipeline.run(nodes=nodes, show_progress=True)
        index.insert_nodes(processed_nodes)

        del docs, nodes, processed_nodes
        gc.collect()

    def run(self) -> VectorStoreIndex:
        """End to end: embed → index → return."""
        return self.embed_docs()
