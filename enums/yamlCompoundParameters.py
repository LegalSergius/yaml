from .customEnum import CustomEnum
from enum import auto
# from utils import yaml_repr_implementation, yaml_repr_field_implementation
import utils


class YAMLCommonParameters(CustomEnum):
    MAX_LENGTH = auto()
    MIN_LENGTH = auto()
    MULTIPLE_OF = auto()

    def yaml_repr(self):
        return utils.yaml_repr_implementation(self)
        

class YAMLFieldAndQueryParameters(CustomEnum):
    # DEFAULT = auto()
    MAX_ITEMS = auto()
    MIN_ITEMS = auto()
    PATTERN = auto()
    UNIQUE_ITEMS = auto()

    def yaml_repr(self):
        return utils.yaml_repr_implementation(self)


class YAMLCustomParameters(CustomEnum):
    EXCLUSIVE_MAXIMUM = 'lt'
    EXCLUSIVE_MINIMUM = 'gt'
    MAXIMUM = 'le'
    MINIMUM = 'ge'

    def yaml_repr(self):
        return utils.yaml_repr_field_implementation(self)


    # def __str__(self):
    #     return '_'.join(*(part.lower() for part in self.name.split('_')))