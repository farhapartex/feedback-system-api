from pydantic import BaseModel


class PostFeedbackDTO(BaseModel):
    topic: str
    description: str

