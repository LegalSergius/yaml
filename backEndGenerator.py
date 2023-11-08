from os import mkdir
from os.path import join
from jinjaResolver import JinjaResolver
from enums.yamlCommonTags import YAMLCommonTags, YAMLRepresentationTags, YAMLExclusiveTags
from enums.yamlDataTypes import YAMLDataTypes
from enums.yamlCompoundTags import YAMLCompoundTags
from enums.mappings import YAML_PROPERTIES_MAPPING, YAML_TYPE_CUSTOM_MAPPING
from enums.yamlDataFormats import YAMLDataFormats

import utils
import yamlParser



class BackEndGenerator:
    # class ModelWriter:
    #     def __init__(self, models_directory, class_name, module_name):
    #         self.__new_import_line = f'from .{module_name} import {class_name}'
    #         self.__model_file_path = join(models_directory, f'{module_name}.py')


    #     def write_import_line_to_init_file(self, init_file_path):
    #         with open(init_file_path, 'r+', encoding='utf-8') as init_file:
    #             lines = init_file.readlines()
    #             self.__new_import_line += '\n'

    #             if self.__new_import_line not in lines:
    #                 init_file.write(self.__new_import_line)

        
    #     def write_model(self, deffered_import_models, rendered_model):
    #         with open(self.__model_file_path, 'w', encoding='utf-8') as model_file:
    #             if len(deffered_import_models):
    #                 lines = [line + '\n' for line in rendered_model.splitlines()]
    #                 last_import_line_index = utils.get_last_import_line(lines)

    #                 generated_lines = utils.generate_model_import_lines(last_import_line_index, lines, deffered_import_models)

    #                 model_file.truncate()
    #                 model_file.writelines(generated_lines)
    #             else:
    #                 model_file.write(rendered_model)
    

    # __DESCRIPTION = str(yamlParser.YAMLTags.DESCRIPTION)
    # __NAME = str(yamlParser.YAMLTags.NAME)
    # __PROPERTIES = str(yamlParser.YAMLTags.PROPERTIES)
    # __REF_SIGN = str(yamlParser.YAMLTags.REF_SIGN)
    # __TYPE = str(yamlParser.YAMLTags.TYPE)
    __DESCRIPTION = YAMLCommonTags.DESCRIPTION.yaml_repr()
    __NAME = YAMLExclusiveTags.NAME.yaml_repr()
    __PROPERTIES = YAMLCommonTags.PROPERTIES.yaml_repr()
    __REF_SIGN = YAMLCommonTags.REF_SIGN.yaml_repr()
    __TYPE = YAMLExclusiveTags.TYPE.yaml_repr()


    def __init__(self, output_directory, yaml_content_dict):
        self.__yaml_content_dict = yaml_content_dict
        self.__models_directory = join(output_directory, 'models')
        self.__enums_directory = join(output_directory, 'enums')
        self.__init_file = join(self.__models_directory, '__init__.py')
        # self.__deffered_import_models = list()
        self.__deffered_import_models = dict()
        self.__defined_parameters = dict()

        self.__create_directories_and_init_file()

    @property
    def deffered_import_models(self):
        return self.__deffered_import_models
    
    
    def __create_directories_and_init_file(self):
        if not utils.validate_dir_existence(self.__models_directory):
            mkdir(self.__models_directory)
        if not utils.validate_dir_existence(self.__enums_directory):
            mkdir(self.__enums_directory)
            
        with open(self.__init_file, 'w', encoding='utf-8') as _:
            pass


    def generate_models(self):
        for component, info in self.__yaml_content_dict.get_schemas().items():
            self.__handle_model_info(component, info)

    
    def __create_enum(self, module_name, class_name, info):
        enum_template = JinjaResolver('enum_template', info=info, class_name=class_name)
        rendered_enum_class = enum_template.release_template()

        model_file_path = join(self.__enums_directory, f'{module_name}.py')

        with open(model_file_path, 'w', encoding='utf-8') as model_file:
            model_file.write(rendered_enum_class)
    

    # def __check_requirement(self, property, property_type, required_fields, /, *, array_generic_value=''):
    # def __check_requirement(self, property, property_type, required_fields, *, array_generic_value='', field_none_flag=False):
    def __check_requirement(self, is_property_required, property_type, *, array_generic_value='', field_none_flag=False):
        if array_generic_value:
            capitalized_generic_value = utils.capitalize_properly(utils.get_last_splitted(array_generic_value))
            self.__add_import('.', capitalized_generic_value)
            property_type = f'list[{capitalized_generic_value}]'

        # if required_fields and property in required_fields and not field_none_flag:
        if is_property_required:
            return property_type
        
        self.__add_import('typing', 'Optional')
        return f'Optional[{property_type}]'


    def __add_import(self, module, model):
        if module in self.__deffered_import_models:
            self.__deffered_import_models[module].add(model)
        else:
            self.__deffered_import_models[module] = {model}
        # self.__deffered_import_models.append((module, model))

        
    def __type_mapping(self, openapi_type):
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

    def __get_from_mapped_type(self, openapi_type, property, class_name, insights, required_fields):
        # type_object = yamlParser.YAMLDataTypes.return_type_presentation(openapi_type)
        # type_object = YAMLDataTypes.return_type_presentation(openapi_type)
        type_object = YAMLDataTypes.yaml_repr_pairs().get(openapi_type)

        # current_field_info = utils.field_info(required_flag, insights)
        current_field_info = utils.field_info(required_fields and property in required_fields, insights)
        property_value, python_type = '', ''

        match type_object:
            # case yamlParser.YAMLDataTypes.ARRAY:
            case YAMLDataTypes.ARRAY:
                array_items = insights.get(str(yamlParser.YAMLTags.ITEMS))
                property_class_type = class_name + utils.capitalize_properly(property)
                property_value = f"{self.__check_requirement(property, property_class_type, required_fields, array_generic_value=array_items[self.__REF_SIGN])} = {current_field_info}"
            
                return property_value
            # case yamlParser.YAMLDataTypes.BOOLEAN:
            case YAMLDataTypes.BOOLEAN:
                python_type = bool.__name__
            # case yamlParser.YAMLDataTypes.INTEGER:
            case YAMLDataTypes.INTEGER:
                python_type = int.__name__
            # case yamlParser.YAMLDataTypes.NULL:
            case YAMLDataTypes.NULL:
                python_type = 'None'
            # case yamlParser.YAMLDataTypes.NUMBER:
            case YAMLDataTypes.NUMBER:
                python_type = float.__name__
            # case yamlParser.YAMLDataTypes.OBJECT:
            case YAMLDataTypes.OBJECT:
                property_class_type = class_name + utils.capitalize_properly(property)
                property_value = f"{self.__check_requirement(property, property_class_type, required_fields)} = {current_field_info}"
                
                self.__handle_model_info(property, insights, associated_model_name=class_name)
                self.__add_import('.', property_class_type)

                return property_value
            # case yamlParser.YAMLDataTypes.STRING:
            case YAMLDataTypes.STRING:
                python_type = str.__name__

        property_value = f"{self.__check_requirement(property, python_type, required_fields)} = {current_field_info}"
            
        return property_value


    def __add_parameter_info(self, parameter_info):
        self.__defined_parameters = parameter_info.copy()

    
    def __create_parameter_string(self, parameter_name, parameter_info):
        # is_property_required = YAMLCommonTags.REQUIRED.yaml_repr()
    
        copied_parameter_info = parameter_info.copy()

        is_property_required = copied_parameter_info.pop(YAMLExclusiveTags.REQUIRED.yaml_repr(), True)
    
        if YAMLCommonTags.SCHEMA.yaml_repr() in parameter_info:
            copied_parameter_info.update(parameter_info.pop(YAMLCommonTags.SCHEMA.yaml_repr()))

        # property_value = self.__get_property_value(YAMLRepresentationTags.QUERY.yaml_repr(), 
        #     is_property_required, parameter_name, parameter_info)
        property_value = self.__get_property_value(YAMLRepresentationTags.QUERY.yaml_repr(), 
            is_property_required, parameter_name, copied_parameter_info)

        return f'\n\t{parameter_name}: {property_value},'
        # parameter_type = self.__type_mapping(parameter_info[str(yamlParser.YAMLTags.SCHEMA)][self.__TYPE])
        # is_parameter_required_flag = 'required' in parameter_info

        # type_requirement = parameter_type if is_parameter_required_flag else f'Optional[{parameter_type}]'
        # query_requirement = '...' if is_parameter_required_flag else 'None'

        # return (f"""\n\t{parameter_name}: {type_requirement} = Query({query_requirement}, 
        #         alias='{parameter_name}', description='{parameter_info['description']}'),""")


    def set_parameters(self, inner_parameters, outer_parameters=None):
        result_parameters_string = ''
        
        if not len(self.__defined_parameters) and outer_parameters:
            self.__add_parameter_info(outer_parameters)

        for parameter in inner_parameters:
            if self.__REF_SIGN in parameter:
                parameter_id = utils.get_last_splitted(parameter[self.__REF_SIGN])
                if parameter_id in self.__defined_parameters:
                    defined_parameter = self.__defined_parameters[parameter_id]
                    defined_parameter_name = defined_parameter[self.__NAME]
                    # print(f'{inner_parameters=}', f'{outer_parameters=}')
                    result_parameters_string += self.__create_parameter_string(defined_parameter_name, defined_parameter)
            else:
                defined_parameter_name = parameter[self.__NAME]
                result_parameters_string += self.__create_parameter_string(defined_parameter_name, parameter)

        return result_parameters_string
    

    def __retrieve_response_name(self, status, entry, path):
        path_name_parts = path[1:].split('-')
        capitalized_name_parts = (part.capitalize() for part in path_name_parts[1:])
        model_name = ''.join([path_name_parts[0], *capitalized_name_parts, status, 'Response'])
        # print('Model name 1:', model_name)

        self.__handle_model_info(model_name, entry)
        model_name = utils.capitalize_properly(model_name)
        # print('Model name 2:', model_name)

        return model_name
    

    def get_response_models(self, model_paths):
        DESCRIPTION = YAMLCommonTags.DESCRIPTION.yaml_repr()

        response_models = dict()
        
        for path, info in model_paths.items():
            response_models[path] = dict()
            for method, method_info in info.items():
                # success_responses = method_info[str(yamlParser.YAMLTags.RESPONSES)]['200']
                # success_responses = method_info[str(YAMLCommonTags.RESPONSES)]['200']
                response_info = method_info[YAMLCommonTags.RESPONSES.yaml_repr()]
                actual_info = dict()
                responses_set = set()

                success_response = response_info['200']
                model_entry = success_response['content']['application/json']['schema']
                model_name = ''
                
                if self.__REF_SIGN in model_entry:
                    model_name = utils.capitalize_properly(utils.get_last_splitted(model_entry[self.__REF_SIGN]))
                else:
                    # path_name_parts = path[1:].split('-')
                    # capitalized_name_parts = (part.capitalize() for part in path_name_parts[1:])
                    # model_name = ''.join([path_name_parts[0], *capitalized_name_parts, 'Response'])
                    # print('Model name 1:', model_name)

                    # self.__handle_model_info(model_name, model_entry)
                    # model_name = utils.capitalize_properly(model_name)
                    # print('Model name 2:', model_name)
                    model_name = self.__retrieve_response_name('200', model_entry, path)
                
                actual_info['success_model'] = model_name
                responses_set.add(model_name)

                response_info.pop('200')

                status_info = dict()

                for status, content in method_info[YAMLCommonTags.RESPONSES.yaml_repr()].items():
                    content_info = dict()

                    content_info[DESCRIPTION] = content[DESCRIPTION]

                    if 'content' in content:
                        entry = content['content']['application/json']['schema']
                        # print(f'{entry=}')

                        if self.__REF_SIGN in entry:
                            response_name = utils.capitalize_properly(utils.get_last_splitted(entry[self.__REF_SIGN]))
                        else:
                            response_name = self.__retrieve_response_name(status, entry, path)

                        content_info['model'] = response_name
                        responses_set.add(response_name)
                    # actual_info[status] = content_info
                    status_info[status] = content_info

                actual_info['responses'] = status_info

                if len(responses_set) > 1:
                    self.__add_import('typing', 'Union')
                    output_return_value = f'Union[{', '.join(responses_set)}]'
                else:
                    output_return_value, = responses_set

                actual_info['return_value'] = output_return_value
                response_models[path][method] = actual_info

        return response_models
    

    def __parse_properties(self, type_condition_content_dict, class_name='', property=''):
        # for type in enumerated_types:
        #     pass
        # popped_type = type_condition_content_dict.pop(str(yamlParser.YAMLTags.TYPE))
        copied_type_condition_content = type_condition_content_dict.copy()
        # print(f'{copied_type_condition_content=}')
        # if self.__TYPE not in type_condition_content_dict:
        if self.__TYPE not in copied_type_condition_content:
            # type_schema = type_condition_content_dict.get(YAMLCommonTags.SCHEMA.yaml_repr())
            type_schema = copied_type_condition_content.pop(YAMLCommonTags.SCHEMA.yaml_repr())
            # type_condition_content_dict = type_schema.copy()
            copied_type_condition_content = type_schema.copy()

        # popped_type = type_condition_content_dict.pop(self.__TYPE)
        popped_type = copied_type_condition_content.pop(self.__TYPE)
        # yaml_type_object = yamlParser.YAMLDataTypes.field(popped_type)
        
        # yaml_type_object = YAMLDataTypes.field(popped_type)
        yaml_type_object = YAMLDataTypes.yaml_repr_pairs().get(popped_type)
        parsed_properties_info = dict()

        # for key, value in type_condition_content_dict.items():
        for key, value in copied_type_condition_content.items():
            # type_properties = yamlParser.YAML_PROPERTIES_MAPPING[yaml_type_object]
            
            if key == YAMLCommonTags.FORMAT.yaml_repr():
                updated_type, new_module_import, new_class_import = YAMLDataFormats.match_format(value)
                
                if new_module_import and new_class_import:
                    self.__add_import(new_module_import, new_class_import)

                return updated_type
            
            if yaml_type_object in YAML_PROPERTIES_MAPPING:
                type_properties = YAML_PROPERTIES_MAPPING[yaml_type_object]
                
                for property_object in type_properties:
                    represented_property = property_object.yaml_repr()

                    if key == represented_property:
                        parsed_properties_info[str(property_object)] = value

        # custom_yaml_type_object = yamlParser.YAML_TYPE_CUSTOM_MAPPING[yaml_type_object]
        if not len(parsed_properties_info):
            # output_python_type = str(YAMLDataTypes.yaml_repr_pairs().get(popped_type))
            popped_type = YAMLDataTypes.yaml_repr_pairs().get(popped_type)

            match popped_type:
                case YAMLDataTypes.ARRAY:
                    # array_items = type_condition_content_dict.get(str(yamlParser.YAMLTags.ITEMS))
                    array_items = copied_type_condition_content.get(YAMLCommonTags.ITEMS.yaml_repr())
                    capitalized_generic_value = utils.capitalize_properly(utils.get_last_splitted(array_items[self.__REF_SIGN]))
                    output_python_type = f'{str(YAMLDataTypes.ARRAY)}[{capitalized_generic_value}]'

                    self.__add_import('.', capitalized_generic_value)
                    self.__add_import('typing', str(YAMLDataTypes.ARRAY))
                case YAMLDataTypes.OBJECT:
                    output_python_type = class_name + utils.capitalize_properly(property)
                    self.__handle_model_info(property, type_condition_content_dict, associated_model_name=class_name)
                    # self.__handle_model_info(property, copied_type_condition_content, associated_model_name=class_name)
                    self.__add_import('.', output_python_type)
                case _:
                    output_python_type = str(popped_type)

            # return popped_type
            return output_python_type
        
        custom_yaml_type_object = YAML_TYPE_CUSTOM_MAPPING[yaml_type_object]
        self.__add_import('pydantic', str(custom_yaml_type_object))
        
        return custom_yaml_type_object.add_parameters(parsed_properties_info)
    

    def __check_condition(self, condition):
        null_flag = False
        checked_type = ''

        if self.__REF_SIGN in condition:
            capitalized_reference_value = utils.capitalize_properly(utils.get_last_splitted(condition[self.__REF_SIGN]))
            self.__add_import('.', capitalized_reference_value)

            return null_flag, capitalized_reference_value
        
        condition_type = condition[self.__TYPE]
        if condition_type == YAMLDataTypes.NULL.yaml_repr():
            null_flag = True
        elif condition_type in YAMLDataTypes.yaml_repr_pairs().keys():
            checked_type = self.__parse_properties(yamlParser.ContentDict(condition))

        return null_flag, checked_type


    def __check_type_conditions(self, insights, class_name, property):
        custom_type = ''
        null_flag = False
        property_conditions = insights.get(YAMLCompoundTags.ANY_OF.yaml_repr())

        if property_conditions:
            enumerated_types = list()

            for condition in property_conditions:
                # if self.__REF_SIGN in condition:
                #     capitalized_reference_value = utils.capitalize_properly(utils.get_last_splitted(condition[self.__REF_SIGN]))
                #     self.__add_import('.', capitalized_reference_value)

                #     enumerated_types.append(capitalized_reference_value)

                #     continue

                # condition_type = condition[self.__TYPE]
                # if condition_type == YAMLDataTypes.NULL.yaml_repr():
                #     null_flag = True
                # elif condition_type in YAMLDataTypes.yaml_repr_pairs().keys():
                #     parsed_type_with_properties = self.__parse_properties(yamlParser.ContentDict(condition))
                #     enumerated_types.append(parsed_type_with_properties)
                null_flag, condition_type = self.__check_condition(condition)
                if condition_type:
                    enumerated_types.append(condition_type)

                if len(enumerated_types) > 1:
                    custom_type += f'Union[{', '.join(enumerated_types)}]'
                else:
                    custom_type, = enumerated_types
        else:
            # print(f'{insights=}', f'{class_name=}', f'{property=}')
            custom_type = self.__parse_properties(insights, class_name, property)
        return null_flag, custom_type


    def __get_property_value(self, representation_name, is_property_required, property, property_insights, class_name=''):
        properties_combination = property_insights.get(YAMLCompoundTags.ALL_OF.yaml_repr())
        current_field_info = utils.field_info(is_property_required, property_insights)

        if properties_combination:
            entity_schema_name = utils.get_last_splitted(properties_combination[0][self.__REF_SIGN])
            capitalized_schema_value = utils.capitalize_properly(entity_schema_name)
            self.__add_import('.', capitalized_schema_value)

            # current_field_info = utils.field_info(is_property_required, property_insights)
            checked_requirement = f"{self.__check_requirement(property, capitalized_schema_value)}"
        else:
            # print(f'{representation_name=}', f'{is_property_required=}', f'{property=}', f'{property_insights=}', f'{class_name=}')
            null_flag, property_type = self.__check_type_conditions(property_insights, class_name, property)
                    
            # current_field_info = utils.field_info(is_property_required, property_insights)
            # checked_requirement = self.__check_requirement(property and not null_flag, property_type)
            checked_requirement = self.__check_requirement(is_property_required and not null_flag, property_type)
            # checked_requirement = self.__check_requirement(property, property_type)

        return f'{checked_requirement} = {representation_name}({current_field_info})'


    def __handle_model_info(self, /, model_name, info, *, associated_model_name=''):
        class_name, module_name = utils.define_class_module_names(model_name, associated_model_name)
        
        model_template = JinjaResolver('model_template', class_name=class_name)
        content = yamlParser.ContentDict(info)

        # if content.check_key(str(yamlParser.YAMLTags.ENUM)):
        if content.check_key(YAMLCommonTags.ENUM.yaml_repr()):
            return self.__create_enum(module_name, class_name, info)
            
        if content.check_key(self.__DESCRIPTION):
            model_template.add_content_data('description', content.get(self.__DESCRIPTION))

        model_template.add_content_data(self.__PROPERTIES, dict())

        for property, insights in content.get(self.__PROPERTIES).items():
            # required_flag = content.get(str(yamlParser.YAMLTags.REQUIRED))
            # required_fields = content.get(YAMLCommonTags.REQUIRED.yaml_repr())
            required_fields = content.get(YAMLExclusiveTags.REQUIRED.yaml_repr())
            # property_conditions = insights.get(str(yamlParser.YAMLCompoundTags.ANY_OF))
            # property_conditions = insights.get(YAMLCompoundTags.ANY_OF.yaml_repr())
            # property_importation = insights.get(YAMLCompoundTags.ALL_OF.yaml_repr())

            is_property_required = required_fields and property in required_fields
            property_value = self.__get_property_value(YAMLRepresentationTags.FIELD.yaml_repr(), is_property_required, property, insights, class_name)

            # if property_importation:
            #     entity_schema_name = utils.get_last_splitted(property_importation[0][self.__REF_SIGN])
            #     capitalized_schema_value = utils.capitalize_properly(entity_schema_name)
            #     self.__add_import('.', capitalized_schema_value)

            #     current_field_info = utils.field_info(required_fields and property in required_fields, insights)
            #     property_value = f"{self.__check_requirement(property, capitalized_schema_value, required_fields)} = {current_field_info}"
            # else:
            #     null_flag, property_type = self.__check_type_conditions(insights, class_name, property)
                
            #     current_field_info = utils.field_info(required_fields and property in required_fields, insights)
            #     checked_requirement = self.__check_requirement(property, property_type, required_fields, field_none_flag=null_flag)
            #     property_value = f'{checked_requirement} = {current_field_info}'
            #     # null_flag, property_custom_value = self.__check_type_conditions(property_conditions)

            #     # if property_conditions:
            #     #     current_field_info = utils.field_info(required_fields and property in required_fields, insights)
            #     #     property_value = f"{self.__check_requirement(property, property_custom_value, required_fields, field_none_flag=null_flag)} = {current_field_info}"
            #     # else:
            #     #     property_value = self.__get_from_mapped_type(property_custom_value, property, class_name, insights, required_fields)
            # # elif property_conditions:
            # #     null_flag, property_custom_value = self.__check_type_conditions(property_conditions)
                
            # #     current_field_info = utils.field_info(required_fields and property in required_fields, insights)
            # #     property_value = f"{self.__check_requirement(property, property_custom_value, required_fields, field_none_flag=null_flag)} = {current_field_info}"
            # # else:
            # #     yaml_given_type = insights.get(self.__TYPE)
            # #     property_value = self.__get_from_mapped_type(yaml_given_type, property, class_name, insights, required_fields)
        
            model_template.add_sub_key_to_data(self.__PROPERTIES, property, property_value)

        rendered_model = model_template.release_template()

        self.__add_import('pydantic', 'BaseModel')
        self.__add_import('pydantic', 'Field')
        
        # model_writer = self.ModelWriter(self.__models_directory, class_name, module_name)
        model_writer = FileWriter(self.__models_directory, class_name=class_name, module_name=module_name)
        model_writer.write_import_line_to_init_file(self.__init_file)
        model_writer.write_sequential_data(self.__deffered_import_models, rendered_model)

        self.__deffered_import_models.clear()
        

class FileWriter:
    def __init__(self, models_directory, *, class_name='', module_name=''):
        self.__new_import_line = f'from .{module_name} import {class_name}' if class_name and module_name else ''
        self.__model_file_path = join(models_directory, f'{module_name}.py')

    def write_import_line_to_init_file(self, init_file_path):
        with open(init_file_path, 'r+', encoding='utf-8') as init_file:
            lines = init_file.readlines()
            self.__new_import_line += '\n'

            if self.__new_import_line not in lines:
                init_file.write(self.__new_import_line)

        
    def write_sequential_data(self, deffered_import_models, rendered_data):
        with open(self.__model_file_path, 'w', encoding='utf-8') as model_file:
            if len(deffered_import_models):
                lines = [line + '\n' for line in rendered_data.splitlines()]
                last_import_line_index = utils.get_last_import_line(lines)

                generated_lines = utils.generate_model_import_lines(last_import_line_index, lines, deffered_import_models)

                model_file.truncate()
                model_file.writelines(generated_lines)
            else:
                model_file.write(rendered_data)