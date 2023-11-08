from jinja2 import Environment, FileSystemLoader
from os.path import join


class JinjaResolver:
    def __init__(self, template_name, **yaml_content_dict):
        self.__env = Environment(loader=FileSystemLoader('jinja_templates'))
        self.__env_filters = self.__env.filters
        self.__template_name = f'{template_name}.jinja2'
        self.__yaml_content_dict = yaml_content_dict


    def add_filter(self, filter):
        self.__env_filters[filter.__name__] = filter


    def add_content_data(self, key, value):
        self.__yaml_content_dict[key] = value

    
    def add_sub_key_to_data(self, data, key, value):
        data_dict = self.__yaml_content_dict[data]
        data_dict[key] = value


    def release_template(self):
        template = self.__env.get_template(self.__template_name)
        
        return template.render(**self.__yaml_content_dict)
        

    