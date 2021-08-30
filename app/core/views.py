from flask import request
from flask_restful import Resource

from app import app


class FeedbackPostAPIView(Resource):

    def post(self):
        args = request.get_json(force=True)
        return {"message": "Hello World created!", "status": 200}

