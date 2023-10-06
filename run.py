from jinja2 import Environment, FileSystemLoader
from utils import generate_models, set_parameters, get_response_models, set_responses
import yaml


yaml_data = None

with open('api.yaml', encoding='utf-8') as yaml_file:
    yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

if 'components' in yaml_data:
    generate_models(yaml_data['components']['schemas'])

env = Environment(loader=FileSystemLoader('.'))
env.filters['set_parameters'] = set_parameters
env.filters['set_responses'] = set_responses

template = env.get_template('api_template.jinja2')

rendered_code = template.render(data=yaml_data, response_models=get_response_models(yaml_data['paths']))

with open('./generated_api/api.py', 'w', encoding='utf-8') as api_code:
    api_code.write(rendered_code)