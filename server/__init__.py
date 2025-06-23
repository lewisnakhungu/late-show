# server/__init__.py
from .app import create_app
from .models import db  # Optional, to support `from server import create_app, db` in seed.py