from fastapi import APIRouter

from app.models.schemas import (
    RecommendationRequest,
    ConversationRequest
)

from app.services.recommendation_engine import (
    generate_recommendations
)

from app.services.conversation_generator import (
    generate_conversation_starters
)

router = APIRouter()


@router.post("/recommend")
def recommend_connections(request: RecommendationRequest):

    recommendations = generate_recommendations(
        request.interests,
        request.skills,
        request.profession
    )

    return {
        "recommended_connections": recommendations,
        "reasons": [
            "Similar professional interests",
            "Matching technical skills"
        ]
    }


@router.post("/conversation-starters")
def conversation_starters(request: ConversationRequest):

    suggestions = generate_conversation_starters(
        request.profession,
        request.interests
    )

    return {
        "conversation_starters": suggestions
    }


# =====================================================
# NEW ENDPOINT FOR STREAMLIT FRONTEND
# =====================================================

@router.post("/generate")
def generate(request: dict):

    profession = request.get("profession", "")

    skills = request.get("skills", [])

    interests = request.get("interests", [])

    description = request.get("description", "")

    # Generate recommended networking topics
    topics = generate_recommendations(
        interests,
        skills,
        profession
    )

    # Generate conversation starters
    suggestions = generate_conversation_starters(
        profession,
        interests
    )

    # Include event description as a topic if provided
    if description:
        topics.insert(0, description)

    return {
        "topics": topics,
        "suggestions": suggestions
    }
