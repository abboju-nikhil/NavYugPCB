from ai.pdf_reader import PDFReader
from ai.chunker import TextChunker
from ai.embeddings import Embedder

print("1. Reading PDF...")
reader = PDFReader()
text = reader.read_pdf("knowledge/datasheets/LM340.pdf")

print("2. Chunking Text...")
chunker = TextChunker(chunk_size=1000, chunk_overlap=200)
chunks = chunker.chunk_text(text)
print(f"   Created {len(chunks)} chunks.")

print("3. Initializing Embedder (This may take a moment to download the model on the first run)...")
embedder = Embedder()

print("4. Generating Embeddings for the first 3 chunks...")
# We only test the first 3 chunks to save time for this test
test_chunks = chunks[:3]
vectors = embedder.get_embeddings(test_chunks)

for i, vector in enumerate(vectors):
    print(f"   Chunk {i+1} converted to a vector with {len(vector)} dimensions.")
    print(f"   First 5 values of vector {i+1}: {vector[:5]}")