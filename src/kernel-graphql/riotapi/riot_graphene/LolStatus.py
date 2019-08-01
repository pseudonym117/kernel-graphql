from graphene import Boolean, Field, Int, List, ObjectType, String, Schema

def filter_items(cls: type, values: dict):
    return {
        key: value
        for key, value in values.items()
        if key in dir(cls)
    }

class ShardStatusTranslation(ObjectType):
    locale = String()
    content = String()
    updated_at = String()

    @classmethod
    def build_from_dict(cls, input_dict):
        return ShardStatusTranslation(
            **filter_items(cls, input_dict)
        )

class ShardStatusMessage(ObjectType):
    severity = String()
    author = String()
    created_at = String()
    translations = List(ShardStatusTranslation)
    updated_at = String()
    content = String()
    id = String()

    @classmethod
    def build_from_dict(cls, input_dict):
        translations = input_dict.pop('translations', None)
        return ShardStatusMessage(
            translations=[
                ShardStatusTranslation.build_from_dict(translation)
                for translation in translations
            ] if translations else None,
            **filter_items(cls, input_dict),
        )

class ShardStatusIncident(ObjectType):
    active = Boolean()
    created_at = String()
    id = Int()
    updates = List(ShardStatusMessage)

    @classmethod
    def build_from_dict(cls, input_dict: dict):
        updates = input_dict.pop('updates')
        return ShardStatusIncident(
            updates=[
                ShardStatusMessage.build_from_dict(message)
                for message in updates
            ],
            **filter_items(cls, input_dict),
        )

class ShardStatusService(ObjectType):
    status = String()
    incidents = List(ShardStatusIncident)
    name = String()
    slug = String()

    @classmethod
    def build_from_dict(cls, input_dict: dict):
        incidents = input_dict.pop('incidents', None)
        return ShardStatusService(
            incidents=[
                ShardStatusIncident.build_from_dict(incident)
                for incident in incidents
            ] if incidents else None,
            **filter_items(cls, input_dict),
        )

class ShardStatus(ObjectType):
    name = String()
    region_tag = String()
    hostname = String()
    services = List(ShardStatusService)
    slug = String()
    locales = List(String)

    @classmethod
    def build_from_dict(cls, input_dict):
        services = input_dict.pop('services')
        return ShardStatus(
            services=[
                ShardStatusService.build_from_dict(item)
                for item in services
            ],
            **filter_items(cls, input_dict),
        )