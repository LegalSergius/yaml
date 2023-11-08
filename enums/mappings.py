from .yamlDataTypes import YAMLDataTypes
from .yamlCustomTypes import YAMLCustomTypes
from .yamlDataFormats import YAMLDataFormats
from .yamlCommonTags import YAMLCommonTags
from .yamlCompoundParameters import YAMLCustomParameters, YAMLCommonParameters, YAMLFieldAndQueryParameters


YAML_TYPE_CUSTOM_MAPPING = {
    YAMLDataTypes.STRING: YAMLCustomTypes.CONSTR,
    YAMLDataTypes.INTEGER: YAMLCustomTypes.CONINT
}

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
        YAMLDataFormats.DATETIME,
        YAMLDataFormats.EMAIL,
        YAMLDataFormats.URL,
        YAMLDataFormats.UUID
    )
}

# YAML_FIELD_MAPPING_ENUMS = (YAMLCommonTags, YAMLFieldAndQueryParameters)


INTEGER_AND_NUMBER_PROPERTIES_TUPLE = (
    # YAMLCommonParameters.EXCLUSIVE_MAXIMUM,
    # YAMLCommonParameters.EXCLUSIVE_MINIMUM,
    # YAMLCommonParameters.MAXIMUM,
    # YAMLCommonParameters.MINIMUM, 
    YAMLCustomParameters.EXCLUSIVE_MAXIMUM,
    YAMLCustomParameters.EXCLUSIVE_MINIMUM,
    YAMLCustomParameters.MAXIMUM,
    YAMLCustomParameters.MINIMUM,
    YAMLCommonParameters.MULTIPLE_OF
)

YAML_PROPERTIES_MAPPING = {
    YAMLDataTypes.STRING: (
        YAMLCommonParameters.MAX_LENGTH,
        YAMLCommonParameters.MIN_LENGTH, 
        YAMLFieldAndQueryParameters.PATTERN,     
    ),
    YAMLDataTypes.INTEGER: INTEGER_AND_NUMBER_PROPERTIES_TUPLE,
    YAMLDataTypes.NUMBER: INTEGER_AND_NUMBER_PROPERTIES_TUPLE,
    # YAMLDataTypes.ARRAY: (
    #     YAMLCompoundParameters.MAX_ITEMS,
    #     YAMLCompoundParameters.MIN_ITEMS
    # ),
    YAMLDataTypes.OBJECT: (
        # YAMLCompoundTags.MAX_PROPERTIES,
        # YAMLCompoundTags.MIN_PROPERTIES
    )
}