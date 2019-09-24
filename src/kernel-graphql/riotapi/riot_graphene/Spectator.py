from graphene import Boolean, Field, Int, List, String

from riotwatcher import RiotWatcher, ApiError

from .League import LeagueEntry
from .RiotGrapheneObject import RiotGrapheneObject


class BannedChampion(RiotGrapheneObject):
    pickTurn = Int()
    championId = Int()
    teamId = Int()


class Observer(RiotGrapheneObject):
    encryptionKey = String()


class GameCustomizationObject(RiotGrapheneObject):
    category = String()
    content = String()


class Perks(RiotGrapheneObject):
    perkStyle = Int()
    perkIds = List(Int)
    perkSubStyle = Int()


class CurrentGameParticipant(RiotGrapheneObject):
    profileIconId = Int()
    championId = Int()
    summonerName = String()
    gameCustomizationObjects = List(GameCustomizationObject)
    bot = Boolean()
    perks = Field(Perks)
    spell2Id = Int()
    teamId = Int()
    spell1Id = Int()
    summonerId = String()


class CurrentGameInfo(RiotGrapheneObject):
    gameId = Int()
    gameStartTime = Int()
    platformId = String()
    gameMode = String()
    mapId = Int()
    gameType = String()
    bannedChampions = List(BannedChampion)
    observers = Field(Observer)
    participants = List(CurrentGameParticipant)
    gameLength = Int()
    gameQueueConfigId = Int()
