# app/resources/guest.py
from flask_restful import Resource
from ..models import Guest

class Guests(Resource):
    def get(self):
        guests = Guest.query.all()
        return [g.to_dict() for g in guests], 200

class GuestByID(Resource):
    def get(self, id):
        guest = Guest.query.get(id)
        if not guest:
            return {"error": "Guest not found"}, 404
        return guest.to_dict(), 200