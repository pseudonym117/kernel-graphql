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


class BaseParticipant(RiotGrapheneObject):
    profileIconId = Int()
    championId = Int()
    summonerName = String()
    bot = Boolean()
    spell2Id = Int()
    teamId = Int()
    spell1Id = Int()

    summoner = Field(lambda: Summoner)

    def resolve_summoner(self, info):
        watcher: RiotWatcher = info.context

        summ = watcher.summoner.by_name(self.region, self.summonerName)

        return Summoner(self.region, summ)


class CurrentGameParticipant(BaseParticipant):
    gameCustomizationObjects = List(GameCustomizationObject)
    perks = Field(Perks)
    summonerId = String()


class GameInfo(RiotGrapheneObject):
    gameId = Int()
    gameStartTime = Int()
    platformId = String()
    gameMode = String()
    mapId = Int()
    gameType = String()
    bannedChampions = List(BannedChampion)
    observers = Field(Observer)
    gameLength = Int()
    gameQueueConfigId = Int()


class CurrentGameInfo(GameInfo):
    participants = List(CurrentGameParticipant)


class FeaturedGameInfo(GameInfo):
    participants = List(BaseParticipant)


class FeaturedGames(RiotGrapheneObject):
    clientRefreshInterval = Int()
    gameList = List(FeaturedGameInfo)


from .Summoner import Summoner
