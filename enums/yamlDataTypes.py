from .customEnum import CustomEnum
from enum import auto


class YAMLDataTypes(CustomEnum):
    ARRAY = 'List'
    BOOLEAN = 'bool'
    INTEGER = 'int'
    NULL = 'None'
    NUMBER = 'float'
    OBJECT = auto()
    STRING = 'str'
    UNION = 'Union'
    

    def yaml_repr(self):
        return self.name.lower()
    

