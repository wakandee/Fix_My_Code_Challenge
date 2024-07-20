# api/v1/views/__init__.py
#!/usr/bin/python3
""" Views module """
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *  # Import routes after blueprint is initialized
