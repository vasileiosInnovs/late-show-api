from flask import Flask, logging
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from models import db
from config import SQLALCHEMY_DATABASE_URI

load_dotenv()

jwt = JWTManager()
migrate = Migrate()
api = Api()

def create_app():
    app = Flask(__name__)

    print("✅ Setting up app")
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    #api.init_app(app)

    api = Api(app)

    from controllers.auth_controller import Registration, Login, CheckSession
    from controllers.appearance_controller import Appearances
    from controllers.episode_controller import EpisodesByID, Episodes
    from controllers.guest_controller import Guests

    print("✅ Adding routes...")

    api.add_resource(Registration, '/register')
    api.add_resource(Login, '/login')
    api.add_resource(CheckSession, '/check_session')
    api.add_resource(Appearances, '/appearances')
    api.add_resource(Episodes, '/episodes')
    api.add_resource(EpisodesByID, '/episodes/<int:id>')
    api.add_resource(Guests, '/guests')

    print("✅ App ready")
    print("Registered routes:")
    print(app.url_map)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

