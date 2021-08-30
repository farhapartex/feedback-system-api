from flask import request
from flask_restful import Resource
from pydantic.error_wrappers import ValidationError

from app import app
from app.core.dtos import PostFeedbackDTO
from app.core.services import FeedbackService


class FeedbackPostAPIView(Resource):

    def post(self):
        try:
            request_data = request.get_json(force=True)
            data = PostFeedbackDTO.parse_obj(request_data)
            response = FeedbackService.post_feedback(data=data)
        except ValidationError as error:
            return error.errors(), 400

        return response.dict(), 201

