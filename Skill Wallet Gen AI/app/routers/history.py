from fastapi import APIRouter
from app.services.history_logger import get_history


router = APIRouter()


@router.get("/history")
def history():

    return get_history()
