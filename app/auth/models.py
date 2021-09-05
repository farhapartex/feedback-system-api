from app import db
from app.models import BaseEntity


class Authentication(BaseEntity):
    __tablename__ = "Authentication"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String())
    expired_at = db.Column(db.DateTime())