from enum import StrEnum


class CustomEnum(StrEnum):
    @classmethod
    def types(cls):
        # return tuple(cls.__members__.keys())
        # return tuple(key.lower() for key in cls.__members__.keys())
        return tuple(str(member) for member in cls)
    
    @classmethod
    def output_str_pairs(cls):
        return {str(member): member for member in cls}

    @classmethod
    def yaml_repr_pairs(cls):
        return {member.yaml_repr(): member for member in cls}
    
    @classmethod
    def field(cls, value):
        return cls.pairs().get(value)

    def yaml_repr(self):
        return self.__str__()