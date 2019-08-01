
from . import riotapi

@riotapi.route('/')
def index():
    return 'hello world!'
