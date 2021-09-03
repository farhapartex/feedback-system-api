from app import db
from app.models import BaseEntity


class Feedback(BaseEntity):
    __tablename__ = "Feedback"

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String())
    description = db.Column(db.String())
