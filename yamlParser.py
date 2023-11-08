from yaml import load, FullLoader
from enum import Enum, auto


class YAMLParser:
    def __init__(self, input_file_name):
        self.__input_file_name = input_file_name
        self.__content_dict = ContentDict(self.__load_content(input_file_name))


    def __load_content(self, input_file_name):
        with open(input_file_name, encoding='utf-8') as yaml_file:
            return load(yaml_file, Loader=FullLoader)
             

    @property
    def input_file_name(self):
        return self.__input_file_name
    
    @input_file_name.setter
    def input_file_name(self, new_file_name):
        self.__input_file_name = new_file_name

    @property
    def content_dict(self):
        return self.__content_dict


class ContentDict(dict):
    def __init__(self, content, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(content)
        self.__content = content

        self.__keys = self.__content.keys()


    @property
    def keys(self):
        return self.__keys


    def check_key(self, key):
        return key in self.__keys
    
    
    def get_schemas(self):
        return self.__content.get(str(YAMLTags.COMPONENTS)).get(str(YAMLTags.SCHEMAS))


class CustomEnum(Enum):
    @classmethod
    def types(cls):
        return [str(member) for member in cls]
    
    @classmethod
    def pairs(cls):
        return {str(member): member for member in cls}
    
    @classmethod
    def field(cls, value):
        print(f'{cls.pairs()}')
        return cls.pairs().get(value)

    def __str__(self):
        return self.name.lower()


class YAMLTags(CustomEnum):
    REF_SIGN = '$ref'
    COMPONENTS = auto()
    DESCRIPTION = auto()
    ENUM = auto()
    EXAMPLE = auto()
    FORMAT = auto()
    INFO = auto()
    ITEMS = auto()
    MAXIMUM = auto()
    MINIMUM = auto()
    NAME = auto()
    OPENAPI = auto()
    PARAMETERS = auto()
    PATHS = auto()
    PATTERN = auto()
    PROPERTIES = auto()
    REQUIRED = auto()
    RESPONSES = auto()
    SCHEMA = auto()
    SCHEMAS = auto()
    SERVERS = auto()
    TITLE = auto()
    TYPE = auto()

    def __str__(self):
        if self == YAMLTags.REF_SIGN:
            return self.value
        
        return super().__str__()
    

class YAMLCompoundTags(CustomEnum):
    ALL_OF = auto()
    ANY_OF = auto()
    EXCLUSIVE_MAXIMUM = auto()
    EXCLUSIVE_MINIMUM = auto()
    MAX_ITEMS = auto()
    MAX_LENGTH = auto()
    MAX_PROPERTIES = auto()
    MIN_ITEMS = auto()
    MIN_LENGTH = auto()
    MIN_PROPERTIES = auto()
    MULTIPLE_OF = auto()
    UNIQUE_ITEMS = auto()

    def __str__(self):
        tag_parts = self.name.split('_')
        concatenated_tag_parts = ''.join([tag_parts[0].lower(), *(part.capitalize() for part in tag_parts[1:])])

        return concatenated_tag_parts


class YAMLDataTypes(CustomEnum):
    ARRAY = auto()
    BOOLEAN = auto()
    INTEGER = auto()
    NULL = auto()
    NUMBER = auto()
    OBJECT = auto()
    STRING = auto()
    UNION = auto()

    @classmethod
    def return_type_presentation(cls, given_type):
        if given_type not in cls.types():
            print('Несовпадение типов - ошибка')

        return YAMLDataTypes[given_type.upper()]

    # @classmethod
    # def types(cls):
    #     return [str(member) for member in cls]
    

class YAMLCustomTypes(CustomEnum):
    CONSTR = auto()
    CONINT = auto()

    def add_parameters(self, parameters):
        # print(f'{cls=}')
        print(f'{parameters=}', type(parameters))

        formatted_string = f"{super().__str__()}({', '.join(f'{key}={value}' for key, value in parameters.items())})"

        return formatted_string

    

YAML_TYPE_CUSTOM_MAPPING = {
    YAMLDataTypes.STRING: YAMLCustomTypes.CONSTR,
    YAMLDataTypes.INTEGER: YAMLCustomTypes.CONINT
}


class YAMLDataFormats(CustomEnum):
    BASE64 = 'base64'
    BINARY = 'binary'
    DATE = 'date'
    DATE_TIME = 'date-time'
    DOUBLE = 'double'
    EMAIL = 'email'
    FLOAT = 'float'
    INT32 = 'int32'
    INT64 = 'int64'
    URL = 'url'
    UUID = 'uuid'


YAML_FORMAT_MAPPING = {
    YAMLDataTypes.INTEGER: (
        YAMLDataFormats.INT32,
        YAMLDataFormats.INT64,
    ),
    YAMLDataTypes.NUMBER: (
        YAMLDataFormats.DOUBLE,
        YAMLDataFormats.FLOAT
    ),
    YAMLDataTypes.STRING: (
        YAMLDataFormats.BASE64,
        YAMLDataFormats.BINARY,
        YAMLDataFormats.DATE,
        YAMLDataFormats.DATE_TIME,
        YAMLDataFormats.EMAIL,
        YAMLDataFormats.URL,
        YAMLDataFormats.UUID
    )
}
    

YAML_PROPERTIES_MAPPING = {
    YAMLDataTypes.STRING: (
        YAMLCompoundTags.MAX_LENGTH,
        YAMLCompoundTags.MIN_LENGTH, 
        YAMLTags.PATTERN,     
    ),
    YAMLDataTypes.INTEGER: (
        YAMLCompoundTags.EXCLUSIVE_MAXIMUM,
        YAMLCompoundTags.EXCLUSIVE_MINIMUM,
        YAMLTags.MAXIMUM,
        YAMLTags.MINIMUM, 
        YAMLCompoundTags.MULTIPLE_OF
    ),
    YAMLDataTypes.NUMBER: (
        YAMLCompoundTags.EXCLUSIVE_MAXIMUM,
        YAMLCompoundTags.EXCLUSIVE_MINIMUM,
        YAMLTags.MAXIMUM,
        YAMLTags.MINIMUM, 
        YAMLCompoundTags.MULTIPLE_OF
    ),
    YAMLDataTypes.ARRAY: (
        YAMLCompoundTags.MAX_ITEMS,
        YAMLCompoundTags.MIN_ITEMS
    ),
    YAMLDataTypes.OBJECT: (
        YAMLCompoundTags.MAX_PROPERTIES,
        YAMLCompoundTags.MIN_PROPERTIES
    )
}

