from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Agent Gateway is running!"}

@app.get("/providers")
def list_providers():
    return {
        "providers": [
            "gemini",
            "groq",
            "together",
            "cerebras"
        ]
    }
