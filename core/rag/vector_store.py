import chromadb
from typing import List, Dict, Any

class VectorStore:
    def __init__(self, persist_directory: str = "./vector_db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="engineering_knowledge"
        )

    def add_chunks(self, chunks: List[str], embeddings: List[List[float]], metadatas: List[Dict[str, Any]], ids: List[str]):
        """Stores the text, its mathematical vector, and tracking metadata."""
        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

    def query(self, query_embeddings: List[List[float]], n_results: int = 4) -> dict:
        """Searches the database for the closest matching vectors."""
        return self.collection.query(
            query_embeddings=query_embeddings,
            n_results=n_results
        )