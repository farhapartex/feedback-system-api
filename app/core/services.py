import logging
from typing import Union

from app.core.dtos import PostFeedbackDTO, APISuccessDTO, APIErrorDTO, FeedbackDTO, FeedbackListDTO
from sqlalchemy.sql import text

from app.database import Database

logger = logging.getLogger(__name__)


class FeedbackService:
    @classmethod
    def _handle_value_cleanup(cls, value: str):
        value = value.strip()
        return value.replace("'", "''")

    @classmethod
    def get_feedbacks(cls) -> FeedbackListDTO:
        query = text('SELECT * FROM public."Feedback";')
        result = Database.execute_query(query)
        feedbacks = []
        for row in result:
            row_dict = dict(row)
            feedbacks.append(FeedbackDTO(id=row_dict["id"], topic=row_dict["topic"], description=row_dict["description"]))

        return FeedbackListDTO(feedbacks=feedbacks)

    @classmethod
    def post_feedback(cls, *, data: PostFeedbackDTO) -> Union[APISuccessDTO, APIErrorDTO]:
        query = text(f'INSERT INTO public."Feedback" (topic, description)' + f" VALUES ('{cls._handle_value_cleanup(data.topic)}', '{cls._handle_value_cleanup(data.description)}');")
        Database.execute_query(query)

        return APIErrorDTO(message="Feedback not created, try again after some time", code=500)
