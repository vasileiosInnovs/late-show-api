from flask import Flask, make_response, request, jsonify, session
from flask_restful import Api, Resource
from werkzeug.security import check_password_hash
from flask_jwt_extended import JWTManager, create_access_token

from models import db, User

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'super-secret-key'

jwt = JWTManager(app)

class Registration(Resource):
    def post(self):
        data = request.get_json()

        new_person = User(
            name = data.get('name'),
            password = data.get('_password_harsh')
        )

        db.session.add(new_person)
        db.session.commit()

        new_person_dict = new_person.to_dict()

        response = make_response(
            jsonify(new_person_dict),
            201
        )

        return response
    
api.add_resource(Registration, '/register')

class Login(Resource):
    def post(self):
        data = request.get_json()

        user = User.query.filter_by(name=data.get('name')).first()

        if not user or not check_password_hash(user._password_harsh, data.get('password')):
            return {"error": "Invalid credential"}, 401
        
        access_token = create_access_token(identity=user.id)

        return {"access_token": access_token}, 200
    
api.add_resource(Login, '/login')

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401
        
api.add_resource(CheckSession, '/check_session')