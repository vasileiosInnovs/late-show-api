from flask import jsonify, make_response, request, session
from flask_restful import Resource

from models import db, Appearance, User
from . import api

class Appearances(Resource):
    def post(self):
        data = request.get_json()

        new_appearance = Appearance(
            rating = data.get('rating'),
            guest_id = data.get('guest_id'),
            episode_id = data.get('episode_id')
        )

        db.session.add(new_appearance)
        db.session.commit()

        new_appearance_dict = new_appearance.to_dict()

        response = make_response(
            jsonify(new_appearance_dict),
            201
        )

        return response
    
class CheckSession(Resource):
    def get(self):
        user = User.query.filter_by(id=session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401

api.add_resource(CheckSession, '/check_session')    
api.add_resource(Appearances, '/appearances')