from flask import Flask, make_response, request, jsonify, session
from flask_restful import Resource
from werkzeug.security import check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from . import api

from models import db, User

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret-key'

jwt = JWTManager(app)

class Registration(Resource):
    def post(self):
        data = request.get_json()

        new_person = User(
            username=data.get('username')
        )
        new_person.password = data.get('password')

        db.session.add(new_person)
        db.session.commit()

        new_person_dict = new_person.to_dict()

        return make_response(
            jsonify(new_person_dict),
            201
            )

api.add_resource(Registration, '/register')

class Login(Resource):
    def post(self):
        data = request.get_json()

        user = User.query.filter_by(username=data.get('username')).first()

        if not user or not user.authenticate(data.get('password')):
            return {"error": "Invalid credentials"}, 401

        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, 200

api.add_resource(Login, '/login')

class CheckSession(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401

api.add_resource(CheckSession, '/check_session')