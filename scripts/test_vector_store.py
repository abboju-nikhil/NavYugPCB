from ai.pdf_reader import PDFReader
from ai.chunker import TextChunker
from ai.embeddings import Embedder
from ai.vector_store import VectorStore

print("1. Reading and Chunking PDF...")
text = PDFReader().read_pdf("knowledge/datasheets/LM340.pdf")
chunks = TextChunker(chunk_size=1000, chunk_overlap=200).chunk_text(text)

print("2. Generating Embeddings...")
embedder = Embedder()
embeddings = embedder.get_embeddings(chunks)

print("3. Storing in ChromaDB...")
vector_store = VectorStore(persist_directory="./vector_db")

# ChromaDB requires a unique ID for every chunk, and metadata helps us track the source
ids = [f"lm340_chunk_{i}" for i in range(len(chunks))]
metadatas = [{"source": "LM340.pdf", "chunk_index": i} for i in range(len(chunks))]

# Note: In a production app, you would check if the documents already exist before adding
vector_store.add_chunks(chunks, embeddings, metadatas, ids)
print(f"   Stored {len(chunks)} chunks in ./vector_db")

print("\n4. Testing Semantic Retrieval...")
# Let's ask a specific engineering question
user_query = "What is the maximum output current for this regulator?"
print(f"   Query: '{user_query}'")

# Embed the query using the same model
query_embedding = embedder.get_embedding(user_query)

# Ask ChromaDB for the 2 most relevant chunks
results = vector_store.query([query_embedding], n_results=2)

print("\n--- TOP RESULTS RETRIEVED ---")
for i, doc in enumerate(results['documents'][0]):
    print(f"\nRESULT {i+1} (Source: {results['metadatas'][0][i]['source']}):")
    print(doc)
    print("-" * 50)