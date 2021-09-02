import logging
import json
from flask import request
from flask_restful import Resource
from pydantic.error_wrappers import ValidationError

from app import app
from app.core.dtos import PostFeedbackDTO, ErrorDTO
from app.core.exceptions import QueryExecutionFailException
from app.core.services import FeedbackService
from app.http import http_response

logger = logging.getLogger(__name__)


class FeedbackPostAPIView(Resource):

    def get(self):
        try:
            result = FeedbackService.get_feedbacks()
        except QueryExecutionFailException as error:
            error_dto = ErrorDTO(details=error.details, code=500)
            return http_response(data=error_dto.dict(), code=500)

        return http_response(data=result.dict())

    def post(self):
        try:
            request_data = request.get_json(force=True)
            data = PostFeedbackDTO.parse_obj(request_data)
            result = FeedbackService.post_feedback(data=data)
        except ValidationError as error:
            logger.error(str(error))
            return http_response(data=error.errors(), code=400)
        except QueryExecutionFailException as error:
            error_dto = ErrorDTO(details=error.details, code=500)
            return http_response(data=error_dto.dict(), code=500)

        return http_response(data=result.dict(), code=201)

