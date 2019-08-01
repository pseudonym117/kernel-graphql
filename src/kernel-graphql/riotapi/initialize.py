import os

from flask_graphql import GraphQLView

from riotwatcher import RiotWatcher

from . import riotapi
from .objects import schema

def init():
    kernel = os.getenv('KERNEL_URL')

    watcher = RiotWatcher(kernel_url=kernel)

    from . import views

    riotapi.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, get_context=lambda: watcher, graphiql=True))
