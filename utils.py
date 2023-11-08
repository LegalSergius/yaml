from shutil import rmtree
from yamlParser import ContentDict, YAMLTags
from enums.yamlCommonTags import YAMLCommonTags
from enums.yamlCompoundParameters import YAMLFieldAndQueryParameters
from enums.yamlDataTypes import YAMLDataTypes
from os.path import exists, isdir
# from enums.mappings import YAML_FIELD_MAPPING_ENUMS


def capitalize_properly(target_str):
    return target_str[0].upper() + target_str[1:]


def get_module_style_name(target_str):
    return target_str[0].lower() + target_str[1:]


def get_last_splitted(expression, /, *, splitter='/'):
    return expression.split(splitter)[-1]


def delete_if_dir_exists(directory):
    if validate_dir_existence(directory):
        rmtree(directory)


def validate_dir_existence(directory):
    return exists(directory) and isdir(directory)


def get_last_import_line(file_lines):
    line_counter = 0

    for line in file_lines:
        if not (line.startswith('from ') and 'import' in line) or not line.startswith('import '):
            break

        line_counter += 1
        
    return line_counter


def generate_model_import_lines(last_import_line_index, lines, import_models):    
    for module, models in import_models.items():
        new_import_line = f'from {module} import {', '.join(models)}\n'

        if new_import_line not in lines:
            lines.insert(last_import_line_index, new_import_line)
            last_import_line_index += 1 
            
    return lines


def define_class_module_names(model_name, associated_model_name):
    capitalized_model_name = capitalize_properly(model_name)

    if len(associated_model_name):
        new_model_name = associated_model_name + capitalized_model_name

        return new_model_name, get_module_style_name(new_model_name)
  
    return capitalized_model_name, model_name


def return_if_null_with_type(types_list):
    null_existence = False
    types_count = 0
    yaml_types_list = YAMLDataTypes.types()

    for type in types_list:
        if type == str(YAMLDataTypes.NULL):
            null_existence = True
        elif type in yaml_types_list:
            types_count += 1

    return null_existence, types_count


def field_info(required_flag, field_insights):
    # parameters_string = ''
    parameters = dict()
    field_insights_content = ContentDict(field_insights)
    
    # default_value = field_insights_content.get(YAMLCommonTags.DEFAULT.yaml_repr())
    default_value = field_insights_content.get('default')
    DESCRIPTION = str(YAMLTags.DESCRIPTION)
    EXAMPLE = str(YAMLTags.EXAMPLE)
    NULL = str(YAMLDataTypes.NULL)

    for content_key in field_insights_content.keys:
        for enum in (YAMLCommonTags, YAMLFieldAndQueryParameters):
            repr_object_pairs = enum.yaml_repr_pairs()

            if content_key in repr_object_pairs:
                enum_object = repr_object_pairs[content_key]
            
                value = repr(field_insights_content.get(content_key))

                # if enum_object == YAMLCommonTags.EXAMPLE:
                #     value = repr(value)

                # parameters[content_key] = value
                parameters[str(enum_object)] = value

    # field_requirement = default_value if default_value else str(YAMLDataTypes.NULL) if field_none_flag else '...'
    field_requirement = repr(default_value) if default_value is not None else '...' if required_flag else NULL
    # parameters_string += f"description='{field_insights_content.get(DESCRIPTION)}'" if field_insights_content.check_key(DESCRIPTION) else ''
    # parameters_string += f", example={repr(field_insights_content.get(EXAMPLE))}" if field_insights_content.check_key(EXAMPLE) else ''
    parameters_string = ', '.join([f'{key}={item}' for key, item in parameters.items()])

    return f'{field_requirement}, {parameters_string}'


def yaml_repr_implementation(self):
    return value_representation(super(type(self), self).yaml_repr())


def value_representation(base):
    splited_representation = base.split('_')
    first_part = splited_representation[0]
    capitalized_remaining_parts = (part.capitalize() for part in splited_representation[1:])

    return ''.join((first_part, *capitalized_remaining_parts))


def yaml_repr_field_implementation(self):
    return value_representation(self.name.lower())

    