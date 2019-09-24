from graphene import Boolean, Field, Int, List, ObjectType, String, Schema

from riotwatcher import RiotWatcher

from .riot_graphene.Champion import ChampionInfo
from .riot_graphene.League import ApexLeagueType, LeagueList, RankedQueue
from .riot_graphene.LolStatus import ShardStatus
from .riot_graphene.Summoner import Summoner


class Query(ObjectType):
    champion_rotation = Field(ChampionInfo, region=String())
    league = Field(
        LeagueList,
        region=String(),
        tier=ApexLeagueType(required=False),
        queue=RankedQueue(required=False),
        league_id=String(required=False),
    )
    status = Field(ShardStatus, region=String())
    summoner = Field(
        Summoner,
        region=String(),
        name=String(required=False),
        encrypted_account_id=String(required=False),
        encrypted_puuid=String(required=False),
        encrypted_summoner_id=String(required=False),
    )

    @staticmethod
    def resolve_champion_rotation(root, info, region):
        watcher: RiotWatcher = info.context

        champs = watcher.champion.rotations(region)

        return ChampionInfo(region, champs)

    @staticmethod
    def resolve_league(
        root,
        info,
        region: str,
        tier: int = None,
        queue: int = None,
        league_id: str = None,
    ):
        watcher: RiotWatcher = info.context

        if league_id:
            leagues = watcher.league.by_id(region, league_id)
        else:
            if not queue or not tier:
                raise ValueError("both queue and tier must be provided")

            queue = RankedQueue.str_from_val(queue)

            if tier == ApexLeagueType.CHALLENGER:
                leagues = watcher.league.challenger_by_queue(region, queue)
            elif tier == ApexLeagueType.GRANDMASTER:
                leagues = watcher.league.grandmaster_by_queue(region, queue)
            elif tier == ApexLeagueType.MASTER:
                leagues = watcher.league.masters_by_queue(region, queue)
            else:
                raise ValueError("invalid tier provided")

        return LeagueList(region, leagues)

    @staticmethod
    def resolve_status(root, info, region):
        watcher: RiotWatcher = info.context

        shard = watcher.lol_status.shard_data(region=region)

        return ShardStatus(region, shard)

    @staticmethod
    def resolve_summoner(
        root,
        info,
        region,
        name=None,
        encrypted_account_id=None,
        encrypted_puuid=None,
        encrypted_summoner_id=None,
    ):
        watcher: RiotWatcher = info.context

        if encrypted_puuid:
            summoner = watcher.summoner.by_puuid(region, encrypted_puuid)
        elif encrypted_account_id:
            summoner = watcher.summoner.by_account(region, encrypted_account_id)
        elif encrypted_summoner_id:
            summoner = watcher.summoner.by_id(region, encrypted_summoner_id)
        elif name:
            summoner = watcher.summoner.by_name(region, name)
        else:
            raise ValueError("some identified must be defined")

        return Summoner(region, summoner)


schema = Schema(query=Query)
