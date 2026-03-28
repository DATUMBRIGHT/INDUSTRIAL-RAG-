from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import get_response_synthesizer
from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.core.retrievers import QueryFusionRetriever
from llama_index.core import VectorStoreIndex


class RAGQueryEngine:
    def __init__(self, index: VectorStoreIndex):
        self.index = index

        # ── Retrievers ───────────────────────────────────────
        nodes = list(self.index.docstore.docs.values())

        self.bm25_retriever = BM25Retriever.from_defaults(
            nodes=nodes,
            similarity_top_k=10,
        )
        self.vector_retriever = self.index.as_retriever(
            similarity_top_k=10,
        )

        # ── Fusion retriever ─────────────────────────────────
        self.retriever = QueryFusionRetriever(
            [self.vector_retriever, self.bm25_retriever],
            similarity_top_k=10,
            num_queries=1,
            mode="reciprocal_rerank",
            use_async=True,
            verbose=True,
        )

        # ── Reranker ─────────────────────────────────────────
        self.reranker = SentenceTransformerRerank(
            model="cross-encoder/ms-marco-MiniLM-L-6-v2",
            top_n=5,
        )

        # ── Response synthesizer ─────────────────────────────
        self.response_synthesizer = get_response_synthesizer(
            response_mode="compact",
        )

        # ── Query engine — built once, reused ────────────────
        self.query_engine = RetrieverQueryEngine(
            retriever=self.retriever,
            node_postprocessors=[self.reranker],
            response_synthesizer=self.response_synthesizer,
        )

    def query(self, query_str: str) -> str:
        response = self.query_engine.query(query_str)
        return response
