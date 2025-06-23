from flask import jsonify, make_response, request, session
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from models.appearance import Appearance
from app import api
from models import db

class Appearances(Resource):
    @jwt_required()
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
   
api.add_resource(Appearances, '/appearances')