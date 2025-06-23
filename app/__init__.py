# app/__init__.py
from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate, api
from .config import Config
from .resources import register_resources

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #initialize CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    # Register resources
    register_resources(app)

    return app