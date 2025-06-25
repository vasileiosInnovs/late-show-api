from sqlalchemy_serializer import SerializerMixin
from . import db

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    number = db.Column(db.Integer)

    def __repr__(self):
        return f'<{self.id}, {self.date}, {self.number}>'