from graphene import Boolean, Enum, Field, Int, List, String

from riotwatcher import RiotWatcher

from .RiotGrapheneObject import RiotGrapheneObject


class ApexLeagueType(Enum):
    CHALLENGER = 1
    GRANDMASTER = 2
    MASTER = 3


class RankedQueue(Enum):
    RANKED_SOLO_5x5 = 1
    RANKED_TFT = 2
    RANKED_FLEX_SR = 3
    RANKED_FLEX_TT = 4

    @staticmethod
    def str_from_val(value):
        if value == RankedQueue.RANKED_SOLO_5x5:
            return "RANKED_SOLO_5x5"
        elif value == RankedQueue.RANKED_TFT:
            return "RANKED_TFT"
        elif value == RankedQueue.RANKED_FLEX_SR:
            return "RANKED_FLEX_SR"
        elif value == RankedQueue.RANKED_FLEX_TT:
            return "RANKED_FLEX_TT"
        return str(value)


class MiniSeries(RiotGrapheneObject):
    progress = String()
    losses = Int()
    target = Int()
    wins = Int()


class LeagueItem(RiotGrapheneObject):
    summonerName = String()
    hotStreak = Boolean()
    miniSeries = Field(MiniSeries)
    wins = Int()
    veteran = Boolean()
    losses = Int()
    freshBlood = Boolean()
    inactive = Boolean()
    rank = String()
    summonerId = String()
    leaguePoints = Int()

    summoner = Field(lambda: Summoner)

    def resolve_summoner(self, info):
        watcher: RiotWatcher = info.context

        summ = watcher.summoner.by_id(self.region, self.summonerId)

        return Summoner(self.region, summ)


class LeagueEntry(LeagueItem):
    queueType = String()
    leagueId = String()
    tier = String()


class LeagueList(RiotGrapheneObject):
    leagueId = String()
    tier = String()
    entries = List(LeagueItem)
    queue = String()
    name = String()


from .Summoner import Summoner
