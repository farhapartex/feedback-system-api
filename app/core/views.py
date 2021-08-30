from flask import request
from flask_restful import Resource
from pydantic.error_wrappers import ValidationError

from app import app
from app.core.dtos import PostFeedbackDTO


class FeedbackPostAPIView(Resource):

    def post(self):
        try:
            request_data = request.get_json(force=True)
            data = PostFeedbackDTO.parse_obj(request_data)
        except ValidationError as error:
            return error.errors(), 400

        return data.dict(), 201

