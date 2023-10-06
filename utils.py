from jinja2 import Environment, FileSystemLoader

import os


MODELS_DIRECTORY_PATH = './generated_api/models'
INIT_FILE_PATH = f'{MODELS_DIRECTORY_PATH}/__init__.py'
REF_SIGN = '$ref'

deffered_import_models = list()
defined_parameters = dict()

def clean_models_list():
    global deffered_import_models
    deffered_import_models = []


def capitalize_properly(target_str):
    return target_str[0].upper() + target_str[1:]


def get_module_style_name(target_str):
    return target_str[0].lower() + target_str[1:]


def type_mapping(openapi_type):
    match openapi_type:
        case 'string':
            return str.__name__
        case 'integer':
            return int.__name__
        case 'number':
            return float.__name__
        case 'boolean':
            return bool.__name__
        case 'null':
            return 'None'
        case _:
            return openapi_type


def parse_model_info(parsed_tuple):
    if (isinstance(parsed_tuple, tuple) and len(parsed_tuple) == 3):
        model_name, model_info, associated_model = parsed_tuple

        handle_model_info(model_name, model_info, associated_model_name=associated_model)

    return ''
    

def get_response_models(model_paths):
    response_models = dict()

    for path, info in model_paths.items():
        response_models[path] = dict()
        for method, method_info in info.items():
            success_responses = method_info['responses']['200']
            model_entry = success_responses['content']['application/json']['schema']
            model_name = ''
            
            if REF_SIGN in model_entry:
                model_name = capitalize_properly(model_entry[REF_SIGN].split('/')[-1])
            else:
                path_name_parts = path[1:].split('-')
                model_name = ''.join([path_name_parts[0], *(part.capitalize() for part in path_name_parts[1:]), 'Response'])
                handle_model_info(model_name, model_entry)
            
            response_models[path][method] = model_name

    return response_models


def handle_model_info(model_name, info, *, associated_model_name=''):
    env = Environment(loader=FileSystemLoader('.'))
    env.filters['check_requirement'] = check_requirement
    env.filters['field_info'] = field_info
    env.filters['capitalize_properly'] = capitalize_properly
    env.filters['parse_model_info'] = parse_model_info
    env.filters['add_import'] = add_import
    env.filters['type_mapping'] = type_mapping

    capitalized_model_name = capitalize_properly(model_name)
    class_name, module_name = '', ''

    if len(associated_model_name):
        new_model_name = associated_model_name + capitalized_model_name
        class_name = new_model_name
        module_name = get_module_style_name(new_model_name)
    else:
        class_name = capitalize_properly(model_name)
        module_name = model_name

    template = env.get_template('model_template.jinja2')
    rendered_model = template.render(data=info, class_name=class_name)
    new_import_line = f"from .{module_name} import {class_name}"

    with open(INIT_FILE_PATH, 'r+', encoding='utf-8') as init_file:
        lines = init_file.readlines()
        new_import_line += '\n'

        if new_import_line not in lines:
            init_file.write(new_import_line)

    model_file_path = f'{MODELS_DIRECTORY_PATH}/{module_name}.py'
    
    with open(model_file_path, 'w', encoding='utf-8') as model_file:
        if len(deffered_import_models):
            lines = [line + '\n' for line in rendered_model.splitlines()]
            last_import_line_index = get_last_import_line(lines)

            generated_lines = generate_model_import_lines(last_import_line_index, lines, deffered_import_models)

            model_file.truncate()
            model_file.writelines(generated_lines)
        else:
            model_file.write(rendered_model)

    clean_models_list()


def field_info(input_info):
    is_required_flag, field_insights = input_info
    parameters_string = ''

    field_requirement = '...' if is_required_flag else 'None'
    parameters_string += f", description='{field_insights['description']}'" if 'description' in field_insights else ''
    parameters_string += f", example={repr(field_insights['example'])}" if 'example' in field_insights else ''

    return f'Field({field_requirement}{parameters_string})'


def generate_model_import_lines(last_import_line_index, lines, import_models):
    for module, model in import_models:
        new_import_line = f'from {module} import {capitalize_properly(model)}\n'

        if new_import_line not in lines:
            lines.insert(last_import_line_index, new_import_line)
            last_import_line_index += 1 
        
    return lines


def get_last_import_line(file_lines):
    line_counter = 0

    for line in file_lines:
        if (line.startswith('from ') and ' import ' in line) or line.startswith('import '):
            line_counter += 1
        else:
            break
    
    return line_counter


def check_requirement(properties_info):
    property, property_type, required_fields = properties_info

    if property in required_fields:
        return property_type
    else: 
        add_import(('typing', 'Optional'))
        return f'Optional[{property_type}]'


def add_parameter_info(parameter_info):
    global defined_parameters
    defined_parameters = parameter_info.copy()


def add_import(module_and_model_info):
    module, model_name = module_and_model_info

    deffered_import_models.append((module, model_name))

    return ''


def generate_models(components):
    if not os.path.exists(MODELS_DIRECTORY_PATH) or not os.path.isdir(MODELS_DIRECTORY_PATH):
        os.mkdir(MODELS_DIRECTORY_PATH)

    with open(INIT_FILE_PATH, 'w', encoding='utf-8') as _:
        pass

    for component, info in components.items():
        handle_model_info(component, info)


def create_parameter_string(parameter_name, parameter_info):
    parameter_type = type_mapping(parameter_info['schema']['type'])
    is_parameter_required_flag = 'required' in parameter_info

    type_requirement = parameter_type if is_parameter_required_flag else f'Optional[{parameter_type}]'
    query_requirement = '...' if is_parameter_required_flag else 'None'

    return f"""\n\t{parameter_name}: {type_requirement} = Query({query_requirement}, alias='{parameter_name}', description='{parameter_info['description']}'),"""


def set_parameters(parameters_info):
    inner_parameters, outer_parameters = parameters_info

    result_parameters_string = ''

    if not len(defined_parameters):
        add_parameter_info(outer_parameters)

    for parameter in inner_parameters:
        if REF_SIGN in parameter:
            parameter_id = parameter[REF_SIGN].split('/')[-1]
            if parameter_id in defined_parameters:
                defined_parameter = defined_parameters[parameter_id]
                defined_parameter_name = defined_parameter['name']
                result_parameters_string += create_parameter_string(defined_parameter_name, defined_parameter)
        else:
            defined_parameter_name = parameter['name']
            result_parameters_string += create_parameter_string(defined_parameter_name, parameter)

    return result_parameters_string


def set_responses(response_list):
    return {code: {'description': response_info['description']} for code, response_info in response_list.items()}

