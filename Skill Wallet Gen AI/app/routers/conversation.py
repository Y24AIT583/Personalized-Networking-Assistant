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

