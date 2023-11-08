from datetime import datetime, date
from .customEnum import CustomEnum
from enum import auto


class YAMLDataFormats(CustomEnum):
    BASE64 = auto()
    BINARY = auto()
    DATE = auto()
    DATETIME = 'date-time'
    DOUBLE = auto()
    EMAIL = auto()
    FLOAT = auto()
    INT32 = auto()
    INT64 = auto()
    URL = auto()
    UUID = auto()

    @classmethod
    def match_format(cls, given_format):
        format_object = cls.yaml_repr_pairs()[given_format]

        match format_object:
            case cls.DATE:
                return date.__name__, 'datetime', date.__name__
            case cls.DATETIME:
                datetime_name = datetime.__name__

                return datetime_name, datetime_name, datetime_name
            case _:
                print('Unexpected format')


    # def __str__(self):
    #     if self == YAMLDataFormats.DATETIME:
    #         return 'datetime'
        
    #     return super().__str__()
    
