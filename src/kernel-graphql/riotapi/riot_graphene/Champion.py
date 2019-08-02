from graphene import Int, List

from .RiotGrapheneObject import RiotGrapheneObject

class ChampionInfo(RiotGrapheneObject):
    freeChampionIdsForNewPlayers = List(Int)
    freeChampionIds = List(Int)
    maxNewPlayerLevel = Int()
