from core.rag.embeddings import Embedder
from core.rag.vector_store import VectorStore
from typing import List, Dict, Any

class RAGRetriever:
    def __init__(self, vector_store: VectorStore, embedder: Embedder):
        self.vector_store = vector_store
        self.embedder = embedder

    def retrieve_context(self, query: str, n_results: int = 4) -> List[str]:
        """Takes a natural language query and returns the most relevant text chunks."""
        query_embedding = self.embedder.get_embedding(query)
        results = self.vector_store.query([query_embedding], n_results=n_results)
        
        # Safely extract documents if they exist
        if results and results.get('documents') and results['documents'][0]:
            return results['documents'][0]
        return []
        
    def retrieve_with_metadata(self, query: str, n_results: int = 4) -> Dict[str, Any]:
         """Retrieves chunks along with their source metadata (e.g., PDF filenames)."""
         query_embedding = self.embedder.get_embedding(query)
         return self.vector_store.query([query_embedding], n_results=n_results)