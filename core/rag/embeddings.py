from sentence_transformers import SentenceTransformer
from typing import List

class Embedder:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        # Downloads/caches the model on first run, loads from local disk thereafter
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text: str) -> List[float]:
        """Converts a single string into a vector."""
        return self.model.encode(text).tolist()

    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Converts a list of strings into a list of vectors."""
        return self.model.encode(texts).tolist()