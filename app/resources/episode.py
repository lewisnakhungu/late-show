# app/resources/episode.py
from flask_restful import Resource
from ..models import Episode

class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [e.to_dict() for e in episodes], 200

class EpisodeByID(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return episode.to_dict(), 200