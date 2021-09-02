import json
from app import app


def http_response(*, data: dict, code: int = 200):
    return app.response_class(response=json.dumps(data), status=code, mimetype='application/json')
