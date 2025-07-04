from flask import jsonify, make_response, session
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from app import api
from models import db

from models.episode import Episode

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
    def get(self, id):
        episode = Episode.query.filter_by(id=id).first()

        episode_dict = episode.to_dict()

        response = make_response(
            jsonify(episode_dict),
            200
        )

        return response
    
    @jwt_required()
    def delete(self, id):
        episode = Episode.query.filter(Episode.id == id).first()

        if not episode:
            return make_response(jsonify({"error": "Episode not found"}), 404)

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

api.add_resource(EpisodesByID, '/episodes/<int:id>')