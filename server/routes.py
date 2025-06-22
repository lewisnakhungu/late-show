# routes.py
from flask_restful import Resource, Api
from flask import request
from .models import db, Episode, Guest, Appearance

def register_routes(app):
    api = Api(app)

    # GET /episodes — list all episodes
    class Episodes(Resource):
        def get(self):
            episodes = Episode.query.all()
            return [e.to_dict() for e in episodes], 200

    # GET /guests — list all guests
    class Guests(Resource):
        def get(self):
            guests = Guest.query.all()
            return [g.to_dict() for g in guests], 200

    # POST /appearances — create a guest appearance in an episode
    class Appearances(Resource):
        def post(self):
            data = request.get_json()
            try:
                new_appearance = Appearance(
                    rating=data["rating"],
                    episode_id=data["episode_id"],
                    guest_id=data["guest_id"]
                )
                db.session.add(new_appearance)
                db.session.commit()
                return new_appearance.to_dict(), 201
            except Exception as e:
                db.session.rollback()
                return {"error": str(e)}, 400

    # GET /episodes/<id> — get episode with appearances
    class EpisodeByID(Resource):
        def get(self, id):
            episode = Episode.query.get(id)
            if not episode:
                return {"error": "Episode not found"}, 404
            return episode.to_dict(), 200

    # GET /guests/<id> — get guest with appearances
    class GuestByID(Resource):
        def get(self, id):
            guest = Guest.query.get(id)
            if not guest:
                return {"error": "Guest not found"}, 404
            return guest.to_dict(), 200

    # Register all routes
    api.add_resource(Episodes, "/episodes")
    api.add_resource(Guests, "/guests")
    api.add_resource(Appearances, "/appearances")
    api.add_resource(EpisodeByID, "/episodes/<int:id>")
    api.add_resource(GuestByID, "/guests/<int:id>")
