from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .user import User
from .guest import Guest
from .appearance import Appearance
from .episode import Episode
