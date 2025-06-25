from sqlalchemy_serializer import SerializerMixin
from . import db

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    serialize_rules = ('-appearances.episode',)

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    number = db.Column(db.Integer)

    appearances = db.relationship('Appearance', back_populates='episode', cascade="all, delete")


    def __repr__(self):
        return f'<{self.id}, {self.date}, {self.number}>'