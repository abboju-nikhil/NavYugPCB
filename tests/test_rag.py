import sys
from pathlib import Path

# Ensure python can locate the 'core' folder relative to the root path
sys.path.append(str(Path(__file__).parent.parent))

from core.rag.pdf_reader import PDFReader
from core.rag.chunker import TextChunker
from core.rag.embeddings import Embedder
from core.rag.vector_store import VectorStore
from core.rag.retriever import RAGRetriever

def test_full_rag_pipeline():
    # 1. Target the datasheet in your new knowledge vault
    # Update "LM340.pdf" if your file is named something else!
    pdf_path = Path("knowledge/datasheets/LM340.pdf") 
    db_path = "./vector_db"

    print(f"1. Reading PDF from {pdf_path}...")
    try:
        text = PDFReader().read_pdf(pdf_path)
        print(f"   Success! Extracted {len(text)} characters.")
    except FileNotFoundError:
        print(f"   [ERROR] Could not find {pdf_path}. Make sure the file is in the knowledge/datasheets folder!")
        return

    print("\n2. Chunking text...")
    chunker = TextChunker(chunk_size=1000, chunk_overlap=200)
    chunks = chunker.chunk_text(text)
    print(f"   Created {len(chunks)} chunks.")

    print("\n3. Initializing AI Models (Loading Embeddings & Vector DB)...")
    embedder = Embedder()
    vector_store = VectorStore(persist_directory=db_path)
    
    print("\n4. Generating embeddings and storing in ChromaDB...")
    embeddings = embedder.get_embeddings(chunks)
    
    # Create tracking metadata and unique IDs for the database
    filename = pdf_path.name
    metadatas = [{"source": filename, "chunk_index": i} for i in range(len(chunks))]
    ids = [f"{filename}_chunk_{i}" for i in range(len(chunks))]
    
    vector_store.add_chunks(chunks, embeddings, metadatas, ids)
    print(f"   Successfully stored {len(chunks)} chunks in {db_path}")

    print("\n5. Testing the Retrieval Engine...")
    retriever = RAGRetriever(vector_store, embedder)
    
    # Simulate an engineering query
    test_query = "What is the maximum output current?"
    print(f"   User Query: '{test_query}'")
    
    results = retriever.retrieve_with_metadata(test_query, n_results=2)
    
    print("\n==================================================")
    print("TOP RESULTS RETRIEVED")
    print("==================================================")
    
    if results and results.get('documents') and results['documents'][0]:
        for i, doc in enumerate(results['documents'][0]):
            source = results['metadatas'][0][i]['source']
            print(f"\nRESULT {i+1} (Source: {source}):")
            print(doc)
            print("-" * 50)
    else:
        print("No results found.")

if __name__ == "__main__":
    test_full_rag_pipeline()