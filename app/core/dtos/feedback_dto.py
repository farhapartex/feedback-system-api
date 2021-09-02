from pydantic import BaseModel


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

