from graphene import Int, String

from .RiotGrapheneObject import RiotGrapheneObject

class Summoner(RiotGrapheneObject):
    profile_icon_id = Int()
    name = String()
    puuid = String()
    summoner_level = Int()
    revision_date = Int()
    id = String()
    account_id = String()
