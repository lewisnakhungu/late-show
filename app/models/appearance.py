# app/models/appearance.py
from ..extensions import db

class Appearance(db.Model):
    __tablename__ = "appearances"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)

    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"))
    guest_id = db.Column(db.Integer, db.ForeignKey("guests.id"))

    episode = db.relationship("Episode", back_populates="appearances")
    guest = db.relationship("Guest", back_populates="appearances")

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "episode": self.episode.to_dict(),
            "guest": self.guest.to_dict(),
        }

    def to_dict_simple(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "episode_id": self.episode_id,
            "guest_id": self.guest_id
        }