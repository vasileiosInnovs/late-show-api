from flask_restful import Api, Resource
from app import app

api = Api(app)

from .auth_controller import auth_controller
from .episode_controller import episode_controller
from .guest_controller import guest_controller
from .appearance_controller import appearance_controller
