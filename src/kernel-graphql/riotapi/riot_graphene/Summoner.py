from graphene import Boolean, Field, Int, List, ObjectType, String, Schema

class Summoner(ObjectType):
    profile_icon_id = Int()
    name = String()
    puuid = String()
    summoner_level = Int()
    revision_date = Int()
    id = String()
    account_id = String()

    @classmethod
    def build_from_dict(cls, input_dict: dict):
        return Summoner(
            profile_icon_id=input_dict['profileIconId'],
            name=input_dict['name'],
            puuid=input_dict['puuid'],
            summoner_level=input_dict['summonerLevel'],
            revision_date=input_dict['revisionDate'],
            id=input_dict['id'],
            account_id=input_dict['accountId'],
        )
