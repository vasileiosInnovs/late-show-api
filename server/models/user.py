from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<ID {self.id} | User {self.username}>'

    # Password setter (hashes the password)
    @property
    def password(self):
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, raw_password):
        self._password_hash = generate_password_hash(raw_password)

    # Check if password is correct
    def authenticate(self, raw_password):
        return check_password_hash(self._password_hash, raw_password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }