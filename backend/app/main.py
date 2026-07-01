from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Import our AI modules
from ai.embeddings import Embedder
from ai.vector_store import VectorStore
from ai.llm import EngineeringLLM

app = FastAPI(
    title="NavYugPCB API",
    version="0.2.0",
    description="AI-powered PCB Design Assistant"
)

# Global variables to hold our AI models in memory
embedder = None
vector_store = None
llm = None

@app.on_event("startup")
async def startup_event():
    """Loads the AI models into memory when the server starts."""
    global embedder, vector_store, llm
    print("Initializing AI Engine... (This may take a few seconds)")
    embedder = Embedder()
    vector_store = VectorStore(persist_directory="./vector_db")
    llm = EngineeringLLM(model_name="qwen3.5:4b")
    print("NavYugPCB AI Engine is ONLINE.")

# Define the structure of the incoming request
class ChatRequest(BaseModel):
    query: str

# Define the structure of the outgoing response
class ChatResponse(BaseModel):
    query: str
    answer: str
    sources: list[str]

@app.get("/")
def home():
    return {"message": "NavYugPCB Backend Running. Go to /docs for the API interface."}

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Takes an engineering question, searches the Vector DB, and returns an AI answer."""
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    
    try:
        # 1. Convert query to math (Vector)
        query_embedding = embedder.get_embedding(request.query)
        
        # 2. Search ChromaDB for relevant chunks
        results = vector_store.query([query_embedding], n_results=4)
        retrieved_chunks = results['documents'][0]
        
        # Extract unique sources (e.g., LM340.pdf) to show the user where the data came from
        raw_sources = [meta.get("source", "Unknown") for meta in results['metadatas'][0]]
        unique_sources = list(set(raw_sources))

        # 3. Generate Answer via Ollama
        answer = llm.generate_answer(request.query, retrieved_chunks)
        
        # 4. Return formatted JSON response
        return ChatResponse(
            query=request.query,
            answer=answer,
            sources=unique_sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))