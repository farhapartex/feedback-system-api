import logging
from typing import Union

from app.core.dtos import PostFeedbackDTO, APISuccessDTO, APIErrorDTO
from sqlalchemy.sql import text

from app.database import Database

logger = logging.getLogger(__name__)


class FeedbackService:
    @classmethod
    def _handle_value_cleanup(cls, value: str):
        value = value.strip()
        return value.replace("'", "''")

    @classmethod
    def get_feedbacks(cls, *, data: PostFeedbackDTO):
        query = text('SELECT * FROM "Feedback";')
        result = Database.execute_query(query)
        return data, result

    @classmethod
    def post_feedback(cls, *, data: PostFeedbackDTO) -> Union[APISuccessDTO, APIErrorDTO]:
        query = text(f'INSERT INTO public."Feedback" (topic, description)' + f" VALUES ('{cls._handle_value_cleanup(data.topic)}', '{cls._handle_value_cleanup(data.description)}');")
        result = Database.execute_query(query)
        if result:
            return APISuccessDTO(message="Feedback created successfully", code=201)

        return APIErrorDTO(message="Feedback not created, try again after some time", code=500)
