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

    championMasteryScore = Int()
    championMasteries = List(lambda: ChampionMastery)
    championMastery = Field(lambda: ChampionMastery, championId=Int())
    currentGame = Field(lambda: CurrentGameInfo)
    leagues = Field(List(lambda: LeagueEntry))
    matchlist = Field(lambda: Matchlist)
    thirdPartyCode = String()

    def resolve_championMasteryScore(self, info):
        watcher: RiotWatcher = info.context

        return watcher.champion_mastery.scores_by_summoner(self.region, self.id)

    def resolve_championMasteries(self, info):
        watcher: RiotWatcher = info.context

        masteries = watcher.champion_mastery.by_summoner(self.region, self.id)

        return [ChampionMastery(self.region, mastery) for mastery in masteries]

    def resolve_championMastery(self, info, championId):
        watcher: RiotWatcher = info.context

        mastery = watcher.champion_mastery.by_summoner_by_champion(
            self.region, self.id, championId
        )

        return ChampionMastery(self.region, mastery)

    def resolve_currentGame(self, info):
        watcher: RiotWatcher = info.context

        try:
            game = watcher.spectator.by_summoner(self.region, self.id)
        except ApiError as e:
            if e.response.status_code == 404:
                return None
            raise
        return CurrentGameInfo(self.region, game)

    def resolve_leagues(self, info):
        watcher: RiotWatcher = info.context

        try:
            leagues = watcher.league.by_summoner(self.region, self.id)
        except ApiError as e:
            if e.response.status_code == 404:
                return []
            raise
        return [LeagueEntry(self.region, league) for league in leagues]

    def resolve_matchlist(self, info):
        watcher: RiotWatcher = info.context

        matchlist = watcher.match.matchlist_by_account(self.region, self.accountId)

        return Matchlist(self.region, matchlist)

    def resolve_thirdPartyCode(self, info):
        watcher: RiotWatcher = info.context

        try:
            return watcher.third_party_code.by_summoner(self.region, self.id)
        except ApiError as e:
            if e.response.status_code == 404:
                return None
            raise


from .ChampionMastery import ChampionMastery
from .League import LeagueEntry
from .Match import Matchlist
from .Spectator import CurrentGameInfo
