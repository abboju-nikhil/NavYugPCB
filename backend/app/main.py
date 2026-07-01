from fastapi import FastAPI

app = FastAPI(
    title="NavYugPCB",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to NavYugPCB 🚀",
        "status": "Backend Running"
    }