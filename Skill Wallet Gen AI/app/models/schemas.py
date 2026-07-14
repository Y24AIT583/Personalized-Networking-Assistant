from pydantic import BaseModel, EmailStr
from typing import List


class UserRegistration(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserProfile(BaseModel):
    name: str
    profession: str
    skills: List[str]
    interests: List[str]
    location: str


class RecommendationRequest(BaseModel):
    interests: List[str]
    skills: List[str]
    profession: str


class RecommendationResponse(BaseModel):
    recommended_connections: List[str]
    reasons: List[str]


class ConversationRequest(BaseModel):
    profession: str
    interests: List[str]


class ConversationResponse(BaseModel):
    conversation_starters: List[str]


class EventRecommendationRequest(BaseModel):
    interests: List[str]
    location: str


class EventRecommendationResponse(BaseModel):
    recommended_events: List[str]


class FeedbackRequest(BaseModel):
    feedback: str
    rating: int


class FeedbackResponse(BaseModel):
    message: str