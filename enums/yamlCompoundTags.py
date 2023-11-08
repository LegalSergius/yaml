from utils import yaml_repr_implementation
from .customEnum import CustomEnum
from enum import auto


class YAMLCompoundTags(CustomEnum):
    ALL_OF = auto()
    ANY_OF = auto()
    REQUEST_BODY = auto()


    # def __str__(self):
    #     base_representation = super().__str__()
    #     splited_representation = base_representation.split('_')
    #     first_part = splited_representation[0]
    #     capitalized_remaining_parts = (part.capitalize() for part in splited_representation[1:])

    #     return ''.join((first_part, *capitalized_remaining_parts))
    def yaml_repr(self):
        return yaml_repr_implementation(self)


    
    