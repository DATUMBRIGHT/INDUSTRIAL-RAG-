import gc
import os
from pathlib import Path
from typing import List

from llama_index.core.extractors import SummaryExtractor, TitleExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core import Document, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
import dotenv

dotenv.load_dotenv()

base_path = Path(__file__).parent.parent / "model"

if base_path.exists():
    print(f"base_path: {base_path}")
else:
    print("base_path not found. Please check the path to your model directory.")

# 1 doc at a time — semantic splitter batches all sentences per doc,
# so even 1 large manual can spike RAM. Raise if your manuals are small.
BATCH_SIZE = 1

PERSIST_DIR = Path(__file__).parent.parent / "storage"


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
                    text=f.read(),
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

        semantic_parser = SemanticSplitterNodeParser(
            buffer_size=2,
            breakpoint_percentile_threshold=90,
            embed_model=self.embed_model,
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
            self._process_batch(batch, semantic_parser, pipeline, index)
            batch = []

        if batch:
            self._process_batch(batch, semantic_parser, pipeline, index)

        PERSIST_DIR.mkdir(parents=True, exist_ok=True)
        index.storage_context.persist(persist_dir=str(PERSIST_DIR))
        print(f"Index persisted to {PERSIST_DIR}")

        return index

    def _process_batch(
        self,
        docs: List[Document],
        parser: SemanticSplitterNodeParser,
        pipeline: IngestionPipeline,
        index: VectorStoreIndex,
    ) -> None:
        names = [d.metadata["file_name"] for d in docs]
        print(f"  Batch: {names}")

        nodes = parser.get_nodes_from_documents(docs, show_progress=False)
        processed_nodes = pipeline.run(nodes=nodes, show_progress=True)
        index.insert_nodes(processed_nodes)

        # Release batch memory before the next one
        del docs, nodes, processed_nodes
        gc.collect()

    def run(self) -> VectorStoreIndex:
        """End to end: embed → index → return."""
        return self.embed_docs()
