from sqlalchemy_serializer import SerializerMixin
from . import db
from sqlalchemy.orm import validates

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'

    serialize_rules = ('-episode.appearances', '-guest.appearances',)

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id', ondelete="CASCADE"))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id', ondelete="CASCADE"))

    episode = db.relationship("Episode", back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')

    @validates('rating')
    def validates_rating(self, key, value):
        if value not in range(1, 6):
            raise ValueError("Rating must be between 1 and 5")
        return value

    def __repr__(self):
        return f'<{self.id}, {self.rating}, {self.guest_id}, {self.episode_id}>'