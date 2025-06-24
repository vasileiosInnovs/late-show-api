from flask import jsonify, make_response
from flask_restful import Resource

from models.guest import Guest
from server.app import api

class Guests(Resource):
    def get(self):
        guests = Guest.query.all()

        guests_dict = [guest.to_dict() for guest in guests]

        response = make_response(
            jsonify(guests_dict),
            200
        )

        return response
    
api.add_resource(Guests, '/guests')