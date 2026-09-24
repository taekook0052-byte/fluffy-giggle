import os

from dotenv import load_dotenv
from google import genai

load_dotenv()  # فایل .env رو می‌خونه

MODEL_NAME = "gemini-flash-latest"

def ask_gemini(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Put it in the .env file.")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    return response.text
