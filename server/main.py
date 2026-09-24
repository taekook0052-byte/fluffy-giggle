from fastapi import FastAPI, HTTPException

from server.providers.gemini import ask_gemini
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

@app.get("/ask")
def ask(prompt: str, task: str = "reasoning"):
    # مدل مناسب رو با روتر انتخاب می‌کنیم (فعلاً همه می‌رن به Gemini)
    model = select_model(task)
    try:
        answer = ask_gemini(prompt)
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return {"task": task, "model": model, "answer": answer}
