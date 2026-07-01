class TextChunker:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_text(self, text: str) -> list[str]:
        """Splits a large text string into smaller, overlapping chunks."""
        if not text:
            return []

        chunks = []
        start = 0
        text_length = len(text)

        while start < text_length:
            end = start + self.chunk_size
            
            if end < text_length:
                # Look for the last newline to avoid splitting mid-sentence
                last_newline = text.rfind('\n', start + self.chunk_size - self.chunk_overlap, end)
                if last_newline != -1:
                    end = last_newline + 1 

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            start = end - self.chunk_overlap

        return chunks