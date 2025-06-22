from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Episode, Guest, Appearance  # Adjust import based on your project structure

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def seed_data():
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()

        # Seed Episodes (10 records)
        episodes = [
            Episode(date="2023-01-10", number=101),
            Episode(date="2023-02-15", number=102),
            Episode(date="2023-03-20", number=103),
            Episode(date="2023-04-05", number=104),
            Episode(date="2023-05-12", number=105),
            Episode(date="2023-06-18", number=106),
            Episode(date="2023-07-25", number=107),
            Episode(date="2023-08-30", number=108),
            Episode(date="2023-09-14", number=109),
            Episode(date="2023-10-22", number=110),
        ]
        db.session.add_all(episodes)
        db.session.commit()

        # Seed Guests (10 records)
        guests = [
            Guest(name="Alice Smith", occupation="Data Scientist"),
            Guest(name="Bob Johnson", occupation="Author"),
            Guest(name="Carol Williams", occupation="Entrepreneur"),
            Guest(name="David Brown", occupation="Professor"),
            Guest(name="Emma Davis", occupation="Journalist"),
            Guest(name="Frank Wilson", occupation="Engineer"),
            Guest(name="Grace Lee", occupation="Designer"),
            Guest(name="Henry Martinez", occupation="Musician"),
            Guest(name="Isabella Clark", occupation="Physician"),
            Guest(name="James Taylor", occupation="Consultant"),
        ]
        db.session.add_all(guests)
        db.session.commit()

        # Seed Appearances (10 records)
        appearances = [
            Appearance(rating=8, episode_id=1, guest_id=1),  # Alice on Episode 101
            Appearance(rating=7, episode_id=2, guest_id=2),  # Bob on Episode 102
            Appearance(rating=9, episode_id=3, guest_id=3),  # Carol on Episode 103
            Appearance(rating=6, episode_id=4, guest_id=4),  # David on Episode 104
            Appearance(rating=8, episode_id=5, guest_id=5),  # Emma on Episode 105
            Appearance(rating=7, episode_id=6, guest_id=6),  # Frank on Episode 106
            Appearance(rating=9, episode_id=7, guest_id=7),  # Grace on Episode 107
            Appearance(rating=6, episode_id=8, guest_id=8),  # Henry on Episode 108
            Appearance(rating=8, episode_id=9, guest_id=9),  # Isabella on Episode 109
            Appearance(rating=7, episode_id=10, guest_id=10),  # James on Episode 110
        ]
        db.session.add_all(appearances)
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()