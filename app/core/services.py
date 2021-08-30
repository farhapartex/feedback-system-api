from app.core.dtos import PostFeedbackDTO


class FeedbackService:
    @classmethod
    def post_feedback(cls, *, data: PostFeedbackDTO):
        return data

