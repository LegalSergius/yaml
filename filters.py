from enums.yamlCommonTags import YAMLCommonTags
from utils import capitalize_properly, get_last_splitted

def set_responses(responses):
    # DESCRIPTION = str(YAMLTags.DESCRIPTION)
    DESCRIPTION = YAMLCommonTags.DESCRIPTION.yaml_repr()
    responses.pop('200')

    responses_dict = dict()

    for code, response_info in responses.items():
        response_code_info = dict()

        # pairs = list()
        # pairs.append(f'{repr(DESCRIPTION)}: {repr(response_info[DESCRIPTION])}')
        response_code_info[DESCRIPTION] = response_info[DESCRIPTION]

        response_entry = response_info['content']['application/json']['schema']
        entry_name = get_last_splitted(response_entry[YAMLCommonTags.REF_SIGN.yaml_repr()])
        model_name = capitalize_properly(entry_name)
        # pairs.append(f'{repr('model')}: {model_name}')

        # pairs_string = ', '.join(pairs)
        response_code_info['model'] = model_name

        # pairs_string = ', '.join(pairs)

        response_info[code] = response_code_info

        # responses_dict[code] = f'{{{pairs_string}}}'

    # return {code: {DESCRIPTION: response_info[DESCRIPTION]} for code, response_info in responses.items()}
    return responses_dict
    

def enumerate_tags(tags):
    tags_collection = (repr(tag) for tag in tags)

    return f"[{', '.join(tags_collection)}]"