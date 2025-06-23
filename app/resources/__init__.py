# app/resources/__init__.py
from flask_restful import Api
from .episode import Episodes, EpisodeByID
from .guest import Guests, GuestByID
from .appearance import Appearances

def register_resources(app):
    api = Api(app)
    api.add_resource(Episodes, "/episodes")
    api.add_resource(Guests, "/guests")
    api.add_resource(Appearances, "/appearances")
    api.add_resource(EpisodeByID, "/episodes/<int:id>")
    api.add_resource(GuestByID, "/guests/<int:id>")