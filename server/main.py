from fastapi import FastAPI

from server.router.selector import select_model

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

@app.get("/route")
def route(task: str):
    # task از URL میاد مثلاً: /route?task=code
    model = select_model(task)
    return {"task": task, "model": model}
