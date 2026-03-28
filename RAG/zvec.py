import zvec
import json
from typing import Any, List, Optional
from llama_index.core.vector_stores.types import (
    BasePydanticVectorStore,
    VectorStoreQuery,
    VectorStoreQueryResult,
)
from llama_index.core.schema import BaseNode, TextNode

class ZvecVectorStore(BasePydanticVectorStore):

    stores_text: bool = True

    #  pydantic fields declared at class level
    path: str = "./zvec_vstore"
    collection_name: str = "ab_manuals"
    dim: int = 1536

    _collection: Any = None  # private, excluded from pydantic

    #  pydantic-safe init
    def model_post_init(self, __context: Any) -> None:
        schema = zvec.CollectionSchema(
            name=self.collection_name,
            vectors=zvec.VectorSchema(
                "embedding",
                zvec.DataType.VECTOR_FP32,
                self.dim,           #  dynamic, not hardcoded 4
            ),
            attributes=[
                zvec.AttributeSchema("text",      zvec.DataType.STRING),
                zvec.AttributeSchema("doc_id",    zvec.DataType.STRING),
                zvec.AttributeSchema("file_name", zvec.DataType.STRING),
                zvec.AttributeSchema("metadata",  zvec.DataType.STRING),
            ]
        )
        self._collection = zvec.create_and_open(
            path=self.path, schema=schema
        )

    @property
    def client(self) -> Any:
        return self._collection

    def get(self, text_id: str) -> List[float]:
        # fetch single node by id if needed
        pass

    def add(self, nodes: List[BaseNode], **kwargs) -> List[str]:
        docs = []
        for node in nodes:
            docs.append(
                zvec.Doc(
                    id=node.node_id,                    #  unique per node
                    vectors={"embedding": node.embedding},  #  correct attribute
                    attributes={
                        "text":      node.get_content(),
                        "doc_id":    node.ref_doc_id or "",
                        "file_name": node.metadata.get("file_name", ""),
                        "metadata":  json.dumps(node.metadata),
                    }
                )
            )
        self._collection.insert(docs)
        self._collection.build_index("embedding")
        return [node.node_id for node in nodes]  #  return ids

    def delete(self, ref_doc_id: str, **kwargs) -> None:
        self._collection.delete(ref_doc_id)

    def query(
        self, query: VectorStoreQuery, **kwargs
    ) -> VectorStoreQueryResult:
        
        raw = self._collection.query(
            zvec.VectorQuery(
                "embedding",
                vector=query.query_embedding,   # ✅ actual query vector
            ),
            topk=query.similarity_top_k,        # ✅ dynamic top k
        )

        nodes, similarities, ids = [], [], []
        for r in raw:
            node = TextNode(
                text=r["text"],
                id_=r["id"],
                metadata=json.loads(r["metadata"]),
            )
            nodes.append(node)
            similarities.append(r["score"])
            ids.append(r["id"])

        #  wrap in VectorStoreQueryResult, not raw results
        return VectorStoreQueryResult(
            nodes=nodes,
            similarities=similarities,
            ids=ids,
        )

    def persist(self, persist_path: str, fs=None) -> None:
        pass  # zvec persists to disk automatically