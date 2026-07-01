from ai.pdf_reader import PDFReader
from ai.chunker import TextChunker

# 1. Read the PDF
reader = PDFReader()
text = reader.read_pdf("knowledge/datasheets/LM340.pdf")
print(f"Total extracted characters: {len(text)}")

# 2. Chunk the text
chunker = TextChunker(chunk_size=1000, chunk_overlap=200)
chunks = chunker.chunk_text(text)

print(f"Total chunks created: {len(chunks)}")
print("-" * 50)
print("CHUNK 1:")
print(chunks[0])
print("-" * 50)
print("CHUNK 2:")
print(chunks[1])