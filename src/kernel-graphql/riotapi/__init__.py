from flask import Blueprint

riotapi = Blueprint('riotapi', __name__)

from .initialize import init
