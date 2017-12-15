from authlib.client.apps import (
    twitter, github, google, facebook
)
from ._flask import create_flask_app
from .models import db
from .auth import oauth
from . import routes


def create_app(config=None):
    app = create_flask_app(config)
    db.init_app(app)
    oauth.init_app(app)
    google.register_to(oauth)
    twitter.register_to(oauth)
    github.register_to(oauth)
    facebook.register_to(oauth)
    routes.init_app(app)
    return app
