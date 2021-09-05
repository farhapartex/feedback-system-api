from app import db


class BaseEntity(db.Model):
    __abstract__ = True

    def json(self):
        return self.__dict__

    def __repr__(self):
        return f"ID: {self.id}"