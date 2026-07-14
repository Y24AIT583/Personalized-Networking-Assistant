from fastapi import APIRouter
from app.services.fact_checker import verify_topic


router = APIRouter()


@router.post("/fact-check")
def fact_check(data:dict):

    result = verify_topic(
        data["query"]
    )

    return {
        "summary":result
    }
