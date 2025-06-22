from flask import jsonify, make_response, session
from flask_restful import Resource
from . import api

from models import db, Episode, User

class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()

        episodes_dict = [episode.to_dict() for episode in episodes]

        response = make_response(
            jsonify(episodes_dict),
            200
        )

        return response
    
api.add_resource(Episodes, '/episodes')
    
class EpisodesByID(Resource):
    def delete(self, id):
        episode = Episode.query.filter(Episode.id == id).first()

        db.session.delete(episode)
        db.session.commit()

        response_dict = {
            'delete': 'episode deleted'
        }

        response = make_response(
            jsonify(response_dict),
            200
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
api.add_resource(EpisodesByID, '/episodes/<int:id>')