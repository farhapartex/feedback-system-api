from app import api
from app.core.views import FeedbackPostAPIView

api.add_resource(FeedbackPostAPIView, "/api/v1/post-feedback")

