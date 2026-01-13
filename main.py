from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="Assistant Core API", version="0.1.0")

# === Модели ===
class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str = "assistant-core"
    messages: list[ChatMessage]

class ChatResponse(BaseModel):
    model: str
    choices: list[dict]

# === Эндпоинты ===
@app.get("/health", status_code=200)
async def health_check():
    return {"status": "ok", "service": "assistant-core"}

@app.post("/v1/chat/completions", response_model=ChatResponse)
async def chat_completions(request: ChatRequest):
    # Заглушка – вернём последнее сообщение пользователя
    user_msg = request.messages[-1].content
    reply = f"Assistant-Core received: {user_msg}"
    return {
        "model": request.model,
        "choices": [{"message": {"role": "assistant", "content": reply}}]
    }
