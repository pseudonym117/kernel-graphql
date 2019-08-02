
from collections import OrderedDict

import graphene


class RiotGrapheneObject(graphene.ObjectType):
    __base_types = {graphene.String, graphene.Int, graphene.Boolean, }

    @staticmethod
    def _convert_graphene_field(field_type, arg):
        if isinstance(field_type, graphene.List):
            return [
                RiotGrapheneObject._convert_graphene_field(field_type.of_type, item)
                for item in arg
            ]

        if issubclass(field_type, RiotGrapheneObject):
            return field_type(arg)
            
        if field_type in RiotGrapheneObject.__base_types:
            return arg

    @staticmethod
    def _build_graphene_object_params(fields: OrderedDict, **kwargs):
        to_pass = {}

        for var_name, field in fields.items():
            if var_name in kwargs:
                converted = RiotGrapheneObject._convert_graphene_field(field.type, kwargs[var_name])
                to_pass[var_name] = converted
            else:
                to_pass[var_name] = None
        
        return to_pass

    def __init__(self, input_dict: dict):
        to_pass = RiotGrapheneObject._build_graphene_object_params(self._meta.fields, **input_dict)

        super().__init__(**to_pass)
