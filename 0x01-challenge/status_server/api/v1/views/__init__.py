#!/usr/bin/python3
""" Views module
"""
from api.v1.views import index
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
