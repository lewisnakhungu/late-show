# app/resources/appearance.py
from flask_restful import Resource
from flask import request
from ..extensions import db
from ..models import Appearance

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