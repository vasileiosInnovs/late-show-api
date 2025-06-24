from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from server.models import db

load_dotenv()

jwt = JWTManager()
migrate = Migrate()
api = Api()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    from server.controllers.auth_controller import Registration, Login, CheckSession
    from server.controllers.appearance_controller import Appearances
    from server.controllers.episode_controller import EpisodesByID

    api.add_resource(Registration, '/register')
    api.add_resource(Login, '/login')
    api.add_resource(CheckSession, '/check_session')
    api.add_resource(Appearances, '/appearances')
    api.add_resource(EpisodesByID, '/episodes/<int:id>')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)