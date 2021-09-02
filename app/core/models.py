from app import db


class BaseEntity(db.Model):
    __abstract__ = True

    def json(self):
        return self.__dict__

    def __repr__(self):
        return f"ID: {self.id}"


class Feedback(BaseEntity):
    __tablename__ = "Feedback"

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String())
    description = db.Column(db.String())
