from fastapi import APIRouter
from app.services.feedback_logger import save_feedback

router = APIRouter()


@router.post("/feedback")
def feedback(data: dict):

    save_feedback(data)

    return {
        "message": "Feedback saved successfully."
    }
