from fastapi import FastAPI

from app.routers.conversation import router as conversation_router
from app.routers.feedback import router as feedback_router
from app.routers.history import router as history_router
from app.routers.fact_checker import router as fact_router
from app.routers.generate import router as generate_router

app = FastAPI(
    title="Personalized Networking Assistant",
    description="AI-powered networking assistant using Google Gemini",
    version="1.0.0"
)

#app.include_router(conversation_router)
app.include_router(feedback_router)
app.include_router(history_router)
app.include_router(fact_router)
app.include_router(generate_router)


@app.get("/")
def home():
    return {
        "message": "Personalized Networking Assistant API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
