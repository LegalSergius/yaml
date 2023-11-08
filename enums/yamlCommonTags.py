from .customEnum import CustomEnum
from enum import auto


class YAMLCommonTags(CustomEnum):    
    # ALIAS = auto()
    COMPONENTS = auto()
    # DEFAULT = auto()
    DESCRIPTION = auto()
    ENUM = auto()
    EXAMPLE = auto()
    EXAMPLES = auto()
    FORMAT = auto()
    INFO = auto()
    ITEMS = auto()
    # MAXIMUM = auto()
    # MINIMUM = auto()
    # NAME = auto()
    OPENAPI = auto()
    PARAMETERS = auto()
    PATHS = auto()
    # PATTERN = auto()
    PROPERTIES = auto()
    REF_SIGN = '$ref'
    # REQUIRED = auto()
    RESPONSES = auto()
    SCHEMA = auto()
    SCHEMAS = auto()
    SERVERS = auto()
    TITLE = auto()
    # TYPE = auto()


class YAMLExclusiveTags(CustomEnum):
    ALIAS = auto()
    NAME = auto()
    REQUIRED = auto()
    TYPE = auto()


class YAMLRepresentationTags(CustomEnum):
    FIELD = 'Field'
    QUERY = 'Query'

# class YAMLFieldTags(CustomEnum):
#     DESCRIPTION = auto()
#     EXAMPLE = auto()
#     EXAMPLES = auto()
#     ITEMS = auto()
#     TITLE = auto()