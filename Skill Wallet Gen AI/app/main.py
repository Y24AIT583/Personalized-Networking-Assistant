from fastapi import FastAPI
from app.routers.conversation import router


app = FastAPI(
    title="Personalized Networking Assistant",
    description="AI-powered assistant for generating personalized networking conversations and recommendations.",
    version="1.0.0"
)


# Register conversation APIs
app.include_router(router)


@app.get("/")
def home():
    """
    Root endpoint to check API status.
    """
    return {
        "message": "Personalized Networking Assistant API is running"
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint for deployment monitoring.
    """
    return {
        "status": "healthy"
    }
