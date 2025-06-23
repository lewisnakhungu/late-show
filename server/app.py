#app.py
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from .models import db
from .routes import register_routes
def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = True

    db.init_app(app)
    migrate = Migrate(app, db)

    register_routes(app)
    return app



app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

