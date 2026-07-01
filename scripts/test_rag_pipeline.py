from ai.embeddings import Embedder
from ai.vector_store import VectorStore
from ai.llm import EngineeringLLM

print("1. Initializing AI Engine...")
embedder = Embedder()
# We assume the vectors are already saved in ./vector_db from the previous test
vector_store = VectorStore(persist_directory="./vector_db")
llm = EngineeringLLM(model_name="qwen3.5:4b")

# The user's natural language request
user_query = "What is the maximum output current for the LM340 regulator?"
print(f"\nUser Query: {user_query}")

print("\n2. Searching Engineering Knowledge Base...")
query_embedding = embedder.get_embedding(user_query)

# We pull the top 4 chunks to give Qwen plenty of context
results = vector_store.query([query_embedding], n_results=4)
retrieved_chunks = results['documents'][0]

print("3. Generating Engineering Response (Thinking...)\n")
answer = llm.generate_answer(user_query, retrieved_chunks)

print("=" * 50)
print("NavYugPCB Answer:")
print("=" * 50)
print(answer)
print("=" * 50)