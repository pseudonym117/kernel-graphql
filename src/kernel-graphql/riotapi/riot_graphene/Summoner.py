from graphene import Field, Int, List, String

from riotwatcher import RiotWatcher, ApiError

from .RiotGrapheneObject import RiotGrapheneObject


class Summoner(RiotGrapheneObject):
    profile_icon_id = Int()
    name = String()
    puuid = String()
    summonerLevel = Int()
    revisionDate = Int()
    id = String()
    accountId = String()

    leagues = Field(List(lambda: LeagueEntry))
    currentGame = Field(lambda: CurrentGameInfo)

    def resolve_leagues(self, info):
        watcher: RiotWatcher = info.context

        try:
            leagues = watcher.league.by_summoner(self.region, self.id)
        except ApiError as e:
            if e.response.status_code == 404:
                return []
            raise
        return [LeagueEntry(self.region, league) for league in leagues]

    def resolve_currentGame(self, info):
        watcher: RiotWatcher = info.context

        try:
            game = watcher.spectator.by_summoner(self.region, self.id)
        except ApiError as e:
            if e.response.status_code == 404:
                return None
            raise
        return CurrentGameInfo(self.region, game)


from .League import LeagueEntry
from .Spectator import CurrentGameInfo
