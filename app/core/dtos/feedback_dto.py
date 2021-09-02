from typing import List

from pydantic import BaseModel


class ErrorDTO(BaseModel):
    details: str
    code: int


class PostFeedbackDTO(BaseModel):
    topic: str
    description: str


class APISuccessDTO(BaseModel):
    message: str
    code: int = 200


class APIErrorDTO(BaseModel):
    message: str
    code: int = 200


class QuerySuccessDTO(BaseModel):
    success: bool = True


class QueryFailureDTO(BaseModel):
    error: str


class FeedbackDTO(BaseModel):
    id: int
    topic: str
    description: str


class FeedbackListDTO(BaseModel):
    feedbacks: List[FeedbackDTO]