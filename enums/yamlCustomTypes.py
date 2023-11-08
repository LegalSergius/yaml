from .customEnum import CustomEnum
from enum import auto


class YAMLCustomTypes(CustomEnum):
    CONSTR = auto()
    CONINT = auto()

    def add_parameters(self, parameters):
        formatted_string = f"{super().__str__()}({', '.join(f'{key}={value}' for key, value in parameters.items())})"
        
        return formatted_string