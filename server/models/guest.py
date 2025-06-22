from . import db

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    def __repr__(self):
        return f'<Name {self.name} Occupation {self.occupation}>'