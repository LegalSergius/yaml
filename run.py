from utils import delete_if_dir_exists, capitalize_properly, get_last_splitted
from yamlParser import YAMLParser, YAMLTags
from backEndGenerator import BackEndGenerator, FileWriter
from jinjaResolver import JinjaResolver
from filters import enumerate_tags, set_responses
from argparse import ArgumentParser
from sys import argv, exit
from os import mkdir
from enums.yamlCommonTags import YAMLCommonTags
from enums.yamlCompoundTags import YAMLCompoundTags
from filters import set_responses


def _init(input_file_name, output_directory):
    yaml_parser = YAMLParser(input_file_name=input_file_name)
    content_dict = yaml_parser.content_dict

    delete_if_dir_exists(output_directory)
    mkdir(output_directory)

    COMPONENTS = str(YAMLTags.COMPONENTS)
    # COMPONENTS = YAMLCommonTags.COMPONENTS.value
    PARAMETERS = str(YAMLTags.PARAMETERS)
    # PARAMETERS = YAMLCommonTags.PARAMETERS.value

    if content_dict.check_key(COMPONENTS):
        generator = BackEndGenerator(output_directory, content_dict)
        generator.generate_models()

    # paths_content = content_dict.get(str(YAMLTags.PATHS))
    paths_content = content_dict.get(YAMLCommonTags.PATHS.value)

    generated_template = JinjaResolver('api_template')
    generated_template.add_content_data('paths', paths_content)
    # generated_template.add_content_data('openapi', content_dict.get(str(YAMLTags.OPENAPI)))
    # generated_template.add_content_data('info', content_dict.get(str(YAMLTags.INFO)))
    # generated_template.add_content_data('servers', content_dict.get(str(YAMLTags.SERVERS)))
    generated_template.add_content_data('openapi', content_dict.get(YAMLCommonTags.OPENAPI.value))
    generated_template.add_content_data('info', content_dict.get(YAMLCommonTags.INFO.value))
    generated_template.add_content_data('servers', content_dict.get(YAMLCommonTags.SERVERS.value))
    response_models = generator.get_response_models(paths_content)

    generated_template.add_content_data('response_models', response_models)


    api_parameters = dict()
    responses = dict()

    for path, info in paths_content.items():
        api_parameters[path] = dict()
        responses[path] = dict()

        for method, properties in info.items():
            REQUEST_BODY = YAMLCompoundTags.REQUEST_BODY.yaml_repr()

            if REQUEST_BODY in properties:
                request_body_entry = properties[REQUEST_BODY]['content']['application/json']['schema']
                entry_name = get_last_splitted(request_body_entry[YAMLCommonTags.REF_SIGN.yaml_repr()])
                model_name = capitalize_properly(entry_name)
                # print('Model name: ', model_name)
                api_parameters[path][method] = f'\n\t{entry_name}Body: {model_name},'

                continue

            if PARAMETERS not in properties:
                api_parameters[path][method] = ''
                continue
                
            components = content_dict.get(COMPONENTS)
            # api_parameters[path][method] = generator.set_parameters(properties[PARAMETERS], components[PARAMETERS]) if 'parameters' in properties and 'parameters' in components else ''
            if PARAMETERS in components:
                # parameters_by_path_method = generator.set_parameters(properties[PARAMETERS], outer_parameters=components[PARAMETERS])
                
                print(f'{properties[PARAMETERS]=}', f'{components[PARAMETERS]=}')
                api_parameters[path][method] = generator.set_parameters(properties[PARAMETERS], outer_parameters=components[PARAMETERS])
            else:
                # print(f'2{properties[PARAMETERS]=}', f'2{components[PARAMETERS]=}')
                # parameters_by_path_method = generator.set_parameters(properties[PARAMETERS])
                api_parameters[path][method] = generator.set_parameters(properties[PARAMETERS])

            # responses[path][method] = set_responses(properties[YAMLCommonTags.RESPONSES.yaml_repr()])

            # api_parameters[path][method] = f'{parameters_by_path_method},'
            # api_parameters[path][method] = generator.set_parameters(properties[PARAMETERS], outer_parameters=components[PARAMETERS]) if 'parameters' in properties else ''

    # print(api_parameters)

    generated_template.add_content_data('api_parameters', api_parameters)
    generated_template.add_content_data('opened_bracket', '{')
    generated_template.add_content_data('closed_bracket', '}')
    # generated_template.add_content_data('response_models', generator.get_response_models(paths_content))
    # generated_template.add_filter(set_responses)
    # generated_template.add_content_data('responses', responses)
    generated_template.add_filter(enumerate_tags)

    rendered_code = generated_template.release_template()

    # with open(f'{output_directory}/api.py', 'w', encoding='utf-8') as api_code:
    #     api_code.write(rendered_code)
    model_writer = FileWriter(output_directory, module_name='api')
    model_writer.write_sequential_data(generator.deffered_import_models, rendered_code)


if __name__ == '__main__':
    argument_parser = ArgumentParser(description='Пример использования наименованных параметров.')
    argument_parser.add_argument('--input', '-i', help='Название входного файла с расширением .yaml по стандарту OpenAPI')
    argument_parser.add_argument('--output', '-o', help='Каталог, куда выведется генерируемый Backend по технологии FastAPI')

    if len(argv) == 3:
        input_file_name, output_directory = argv[1], argv[2]
    else:
        parsed_args = argument_parser.parse_args()
        input_file_name, output_directory = parsed_args.input, parsed_args.output

    if not input_file_name:
        print('Для работы программы требуется указать входной файл .yaml!')
        exit(1)
    if not output_directory:
        output_directory = '.'

    _init(input_file_name, output_directory)