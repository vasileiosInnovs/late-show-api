from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance