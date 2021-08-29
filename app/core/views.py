from flask import request
from flask_restful import Resource

from app import app


class HelloWorld(Resource):
    def get(self):
        app.logger.info("working fine")
        return {"message": "Hello World!", "status": 200}

    def post(self):
        args = request.get_json(force=True)
        return {"message": "Hello World created!", "status": 200}

