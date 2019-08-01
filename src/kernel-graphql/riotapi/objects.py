from graphene import Boolean, Field, Int, List, ObjectType, String, Schema

from riotwatcher import RiotWatcher

from .riot_graphene.LolStatus import ShardStatus
from .riot_graphene.Summoner import Summoner

class Query(ObjectType):
    status = Field(ShardStatus, region=String())
    summoner = Field(Summoner, region=String(), name=String(required=False), encrypted_account_id=String(required=False), encrypted_puuid=String(required=False), encrypted_summoner_id=String(required=False))

    def resolve_status(root, info, region):
        watcher: RiotWatcher = info.context

        shard = watcher.lol_status.shard_data(region=region)

        return ShardStatus.build_from_dict(shard)
    
    def resolve_summoner(root, info, region, name=None, encrypted_account_id=None, encrypted_puuid=None, encrypted_summoner_id=None):
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
            raise ValueError('some identified must be defined')
        
        return Summoner.build_from_dict(summoner)

schema = Schema(query=Query)
