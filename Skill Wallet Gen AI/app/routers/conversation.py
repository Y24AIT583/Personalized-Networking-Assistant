from fastapi import APIRouter

from app.models.schemas import (
    RecommendationRequest,
    RecommendationResponse,
    ConversationRequest,
    ConversationResponse,
    FeedbackRequest,
    FeedbackResponse
)

from app.services.recommendation_engine import (
    generate_recommendations
)

from app.services.conversation_generator import (
    generate_conversation_starters
)

from app.services.history_logger import (
    save_history,
    get_history
)

from app.services.feedback_logger import (
    save_feedback
)

router = APIRouter()


@router.post(
    "/recommend",
    response_model=RecommendationResponse
)
def recommend_connections(
        request: RecommendationRequest):

    recommendations = generate_recommendations(
        request.interests,
        request.skills,
        request.profession
    )

    save_history({
        "interests": request.interests,
        "skills": request.skills,
        "profession": request.profession,
        "recommendations": recommendations
    })

    return {
        "recommended_connections": recommendations,
        "reasons": [
            "Similar professional interests",
            "Matching technical skills"
        ]
    }


@router.post(
    "/conversation-starters",
    response_model=ConversationResponse
)
def conversation_starters(
        request: ConversationRequest):

    suggestions = generate_conversation_starters(
        request.profession,
        request.interests
    )

    return {
        "conversation_starters": suggestions
    }


@router.get("/history")
def history():

    return get_history()


@router.post(
    "/feedback",
    response_model=FeedbackResponse
)
def submit_feedback(
        request: FeedbackRequest):

    save_feedback({
        "feedback": request.feedback,
        "rating": request.rating
    })

    return {
        "message": "Feedback submitted successfully."
    }
