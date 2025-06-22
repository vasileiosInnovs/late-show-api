from . import db
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_harsh = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<ID {self.id} | User {self.username}>'
    
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        self._password_harsh = self.simple_hash(password)

    def authenticate(self, password):
        return self.simple_hash(password) == self.password_hash
    
    @staticmethod
    def simple_hash(input):
        return sum(bytearray(input, encoding='utf-8'))