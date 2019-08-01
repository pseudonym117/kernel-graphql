
from flask import Flask


def create_app(config):
    app = Flask(__name__)

    from .riotapi import riotapi, init as riotapi_init
    riotapi_init()

    app.register_blueprint(riotapi)

    return app
