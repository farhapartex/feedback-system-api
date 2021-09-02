import logging
import json
from flask import request
from flask_restful import Resource
from pydantic.error_wrappers import ValidationError

from app import app
from app.core.dtos import PostFeedbackDTO, ErrorDTO
from app.core.exceptions import QueryExecutionFailException
from app.core.services import FeedbackService


logger = logging.getLogger(__name__)


class FeedbackPostAPIView(Resource):

    def get(self):
        try:
            result = FeedbackService.get_feedbacks()
        except:
            pass

        response = app.response_class(response=json.dumps(result.dict()), status=200, mimetype='application/json')
        return response

    def post(self):
        try:
            request_data = request.get_json(force=True)
            data = PostFeedbackDTO.parse_obj(request_data)
            result = FeedbackService.post_feedback(data=data)
        except ValidationError as error:
            return error.errors(), 400
        except QueryExecutionFailException as error:
            return ErrorDTO(details=str(error), code=500), 500

        response = app.response_class(response=json.dumps(result.dict()), status=200, mimetype='application/json')
        return response

