from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.event_analyzer import analyze_profile
from app.services.topic_generator import generate_conversation_topics
from app.services.history_logger import save_history

router = APIRouter()


class GenerateRequest(BaseModel):
    description: str
    interests: List[str]
    skills: List[str]
    profession: str


@router.post("/generate")
def generate(request: GenerateRequest):

    # Step 1: Detect topics from the event description
    detected_topics = analyze_profile(
        request.description
    )

    # Step 2: Generate conversation starters
    suggestions = generate_conversation_topics(
        detected_topics,
        request.interests
    )

    # Step 3: Save history
    try:
        save_history(
            {
                "description": request.description,
                "profession": request.profession,
                "skills": request.skills,
                "interests": request.interests,
                "topics": detected_topics,
                "suggestions": suggestions
            }
        )
        print("✅ History saved successfully")
    except Exception as e:
        print("❌ Error while saving history:", e)

    # Step 4: Return data to Streamlit
    return {
        "topics": detected_topics,
        "suggestions": suggestions
    }
