from . import db
from sqlalchemy.orm import validates

class Appearance(db.Model):
    __tablename__ = 'appearance'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))

    @validates('rating')
    def validates_rating(self, key, value):
        if value not in range(1, 6):
            raise ValueError("Rating must be between 1 and 5")
        return value

    def __repr__(self):
        return f'<{self.id}, {self.rating}, {self.guest_id}, {self.episode_id}>'