from graphene import Int, String

from .RiotGrapheneObject import RiotGrapheneObject

class Summoner(RiotGrapheneObject):
    profile_icon_id = Int()
    name = String()
    puuid = String()
    summonerLevel = Int()
    revisionDate = Int()
    id = String()
    accountId = String()
