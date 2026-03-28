from pathlib import Path
from RAG.chunker import DocChunker
from RAG.queryengine import RAGQueryEngine


if __name__ == "__main__":
    processed_docs_path = Path(__file__).parent / "processed_docs"
    print(f"Processing documents in: {processed_docs_path}")

    chunker = DocChunker(folder_path=processed_docs_path)
    index = chunker.run()

    query_engine = RAGQueryEngine(index=index)

    query = "What are the steps to replace a 1756-UM001-EN-P module in a ControlLogix system?"
    response = query_engine.query(query)
    print(response)
