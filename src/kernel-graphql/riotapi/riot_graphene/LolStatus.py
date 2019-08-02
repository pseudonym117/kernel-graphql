from graphene import Boolean, Int, List, String

from .RiotGrapheneObject import RiotGrapheneObject

class ShardStatusTranslation(RiotGrapheneObject):
    locale = String()
    content = String()
    updated_at = String()

class ShardStatusMessage(RiotGrapheneObject):
    severity = String()
    author = String()
    created_at = String()
    translations = List(ShardStatusTranslation)
    updated_at = String()
    content = String()
    id = String()

class ShardStatusIncident(RiotGrapheneObject):
    active = Boolean()
    created_at = String()
    id = Int()
    updates = List(ShardStatusMessage)

class ShardStatusService(RiotGrapheneObject):
    status = String()
    incidents = List(ShardStatusIncident)
    name = String()
    slug = String()

class ShardStatus(RiotGrapheneObject):
    name = String()
    region_tag = String()
    hostname = String()
    services = List(ShardStatusService)
    slug = String()
    locales = List(String)
