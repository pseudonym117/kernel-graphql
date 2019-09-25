from graphene import Boolean, Field, Int, String

from riotwatcher import RiotWatcher

from .RiotGrapheneObject import RiotGrapheneObject


class ChampionMastery(RiotGrapheneObject):
    chestGranted = Boolean()
    championLevel = Int()
    championPoints = Int()
    championId = Int()
    championPointsUntilNextLevel = Int()
    lastPlayTime = Int()
    tokensEarned = Int()
    championPointsSinceLastLevel = Int()
    summonerId = String()

    summoner = Field(lambda: Summoner)

    def resolve_summoner(self, info):
        watcher: RiotWatcher = info.context

        summ = watcher.summoner.by_id(self.region, self.summonerId)

        return Summoner(self.region, summ)


from .Summoner import Summoner
