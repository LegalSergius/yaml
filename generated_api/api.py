from typing import Union, Optional
from pydantic import conint, constr
from datetime import datetime
from . import IsFalloutType
from fastapi import FastAPI, Query
from fastapi.openapi.utils import get_openapi
from typing import Optional
from models import *
from enums import *

import yaml


contact_info = {
    
    'name': 'VVT Group LLP',
    
    'url': 'http://www.kt.kz/',
    
    'email': 'info@vvt.kz',
    
}

servers_info = [

]

app = FastAPI()

    
@app.post(
    '/api/phone-activate-be/v1.0/request-set-done', 
    response_model=BaseResponse, 
    tags=['BPM activate-phone'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод для BPM Активации Телефонии. Активация/Деактивация выполнена автоматически.')
async def do_phone_activation_request_set_done_api_phone_activate_be_v1_0_request_set_done_post(
	phoneAutomatiSetDoneRequestBody: PhoneAutomatiSetDoneRequest,
) -> BaseResponse:
    """
    Do Phone Activation Request Set Done
    """
    pass
    

    
@app.post(
    '/api/phone-activate-be/v1.0/request-set-fallout', 
    response_model=BaseResponse, 
    tags=['BPM activate-phone'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод для BPM Активации Телефонии. Перевод на ручное исполнение.')
async def do_phone_activation_request_set_fallout_api_phone_activate_be_v1_0_request_set_fallout_post(
	phoneAutomatiSetFalloutRequestBody: PhoneAutomatiSetFalloutRequest,
) -> BaseResponse:
    """
    Do Phone Activation Request Set Fallout
    """
    pass
    

    
@app.get(
    '/api/phone-activate-be/v1.0/get-new-requests-on-exchange-list', 
    response_model=RefExchangeListResponse, 
    tags=['BPM activate-phone'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод для BPM Активации Телефонии. Получение станций по которым есть заявки на автоматическу активацию.')
async def get_new_requests_on_exchange_list_api_phone_activate_be_v1_0_get_new_requests_on_exchange_list_get(
	limit: conint(ge=1) = Query(..., description='Максимальное станций в запросе.', schema={'type': 'integer', 'title': 'limit', 'description': 'Максимальное станций в запросе.', 'minimum': 1, 'examples': [10]}, title='limit', examples=[10]),
) -> Union[RefExchangeListResponse, BaseResponse]:
    """
    Get New Requests On Exchange List
    """
    pass
    

    
@app.get(
    '/api/phone-activate-be/v1.0/get-new-requests-by-exchange-id-list', 
    response_model=AutoActivateListResponse, 
    tags=['BPM activate-phone'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод для BPM Активации Телефонии. Получение заявок для автоматической активацию через ID станции')
async def get_new_requests_by_exchange_id_list_api_phone_activate_be_v1_0_get_new_requests_by_exchange_id_list_get(
	limit: conint(ge=1) = Query(..., description='Максимальное кол-во записей', schema={'type': 'integer', 'title': 'limit', 'description': 'Максимальное кол-во записей', 'minimum': 1, 'examples': [10]}, title='limit', examples=[10]),
	exchangeId: conint(ge=0) = Query(..., description='Ид станции', schema={'type': 'integer', 'title': 'limit', 'description': 'Ид станции', 'minimum': 0, 'examples': [10]}, title='limit', examples=[10]),
) -> Union[BaseResponse, AutoActivateListResponse]:
    """
    Get New Requests By Exchange Id List
    """
    pass
    

    
@app.post(
    '/api/phone-activate-be/v1.0/create-request', 
    response_model=BaseResponse, 
    tags=['BPM OSM/WFM'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Новый запрос на активацию')
async def do_create_phone_activation_request_api_phone_activate_be_v1_0_create_request_post(
	phoneActivateListRequestBody: PhoneActivateListRequest,
) -> BaseResponse:
    """
    Do Create Phone Activation Request
    """
    pass
    

    
@app.post(
    '/api/phone-activate-be/v1.0/assign-request', 
    response_model=BaseResponse, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Назначить заявку, или взять в работу')
async def do_assign_phone_activation_request_api_phone_activate_be_v1_0_assign_request_post(
	phoneAssignRequestBody: PhoneAssignRequest,
) -> BaseResponse:
    """
    Do Assign Phone Activation Request
    """
    pass
    

    
@app.post(
    '/api/phone-activate-be/v1.0/change-fxs-data', 
    response_model=BaseResponse, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Ввод FXS/FXS login')
async def do_change_phone_activation_fxs_data_api_phone_activate_be_v1_0_change_fxs_data_post(
	phoneChangeFxsLoginPwdBody: PhoneChangeFxsLoginPwd,
) -> BaseResponse:
    """
    Do Change Phone Activation Fxs Data
    """
    pass
    

    
@app.post(
    '/api/phone-activate-be/v1.0/manual-execute', 
    response_model=BaseResponse, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Ручное исполнение заявки')
async def do_manual_phone_activation_execute_api_phone_activate_be_v1_0_manual_execute_post(
	phoneManualExecuteRequestBody: PhoneManualExecuteRequest,
) -> BaseResponse:
    """
    Do Manual Phone Activation Execute
    """
    pass
    

    
@app.post(
    '/api/phone-activate-be/v1.0/repeat-auto-activation', 
    response_model=BaseResponse, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Перевод заявки с ручного режима, на потворную активацию.')
async def do_auto_repeat_phone_activation_execute_api_phone_activate_be_v1_0_repeat_auto_activation_post(
	phoneRepeatAutoRequestBody: PhoneRepeatAutoRequest,
) -> BaseResponse:
    """
    Do Auto Repeat Phone Activation Execute
    """
    pass
    

    
@app.get(
    '/api/phone-activate-be/v1.0/get-request', 
    response_model=PhoneActivateFullResponse, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Получение одной записи, для формы детали по заказу')
async def get_phone_activation_request_api_phone_activate_be_v1_0_get_request_get(
	phoneActivateId: conint(ge=0) = Query(..., description='Ид заявки на активацию  ', schema={'type': 'integer', 'title': 'limit', 'description': 'Ид заявки на активацию  ', 'minimum': 0, 'examples': [10]}, title='limit', examples=[10]),
) -> Union[BaseResponse, PhoneActivateFullResponse]:
    """
    Get Phone Activation Request
    """
    pass
    

    
@app.get(
    '/api/phone-activate-be/v1.0/get-request-list', 
    response_model=PhoneActivateSearchListResponse, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод для поиска в GUI')
async def get_phone_activation_request_list_api_phone_activate_be_v1_0_get_request_list_get(
	limit: conint(ge=1) = Query(..., description='Максимальное кол-во записей в поиске', schema={'type': 'integer', 'title': 'limit', 'description': 'Максимальное кол-во записей в поиске', 'minimum': 1, 'examples': [10]}, title='limit', examples=[10]),
	startRow: conint(ge=1) = Query(..., description='Записи с.', schema={'type': 'integer', 'title': 'startRow', 'description': 'Записи с.', 'minimum': 1, 'examples': [1]}, title='startRow', examples=[1]),
	filialId: Optional[int] = Query(None, description='Ид филиала', schema={'type': 'integer', 'title': 'filialId', 'description': 'Ид филиала', 'examples': [5]}, title='filialId', examples=[5]),
	entityId: Optional[int] = Query(None, description='Ид сущности', schema={'type': 'integer', 'title': 'entityId', 'description': 'Ид сущности', 'examples': [22]}, title='entityId', examples=[22]),
	entitySpecId: Optional[int] = Query(None, description='Ид спец сущности entitySpecId', schema={'type': 'integer', 'title': 'entitySpecId', 'description': 'Ид спец сущности entitySpecId', 'examples': [10222221]}, title='entitySpecId', examples=[10222221]),
	customerAccountId: Optional[int] = Query(None, description='Ид лицевого счета', schema={'type': 'integer', 'title': 'entitySpecId', 'description': 'Ид лицевого счета', 'examples': [1022222]}, title='entitySpecId', examples=[1022222]),
	shortNumber: Optional[constr(max_length=50)] = Query(None, description='Короткий номер Телефона', schema={'type': 'string', 'title': 'shortNumber', 'description': 'Короткий номер Телефона', 'maxLength': 50, 'examples': ['22654']}, title='shortNumber', examples=['22654']),
	insertDateFrom: Optional[datetime] = Query(None, description='Дата создания активации с', schema={'type': 'string', 'title': 'insertDateFrom', 'description': 'Дата создания активации с', 'format': 'date-time'}, title='insertDateFrom', format='date-time'),
	insertDateTo: Optional[datetime] = Query(None, description='Дата создания активации по', schema={'type': 'string', 'title': 'insertDateTo', 'description': 'Дата создания активации по', 'format': 'date-time'}, title='insertDateTo', format='date-time'),
	stateId: Optional[int] = Query(None, description='Ид stateId', schema={'type': 'integer', 'title': 'stateId', 'description': 'Ид stateId', 'examples': [1]}, title='stateId', examples=[1]),
	userLogin: Optional[str] = Query(None, description='Логин пользователя', schema={'type': 'string', 'title': 'userLogin', 'description': 'Логин пользователя', 'examples': ['alma-tech']}, title='userLogin', examples=['alma-tech']),
	isFallout: IsFalloutType = Query(None, description='1 - Показать ручные, 0- автоматические, Пусто все', schema={'title': 'isFallout', 'description': '1 - Показать ручные, 0- автоматические, Пусто все', 'examples': ['0,1'], 'allOf': [{'$ref': '#/components/schemas/isFalloutType'}]}, title='isFallout', examples=['0,1']),
	refExchangeIdList: Optional[str] = Query(None, description='refExchangeIdList список станций', schema={'type': 'string', 'title': 'refExchangeIdList', 'description': 'refExchangeIdList список станций', 'examples': ['1,2,33,44']}, title='refExchangeIdList', examples=['1,2,33,44']),
	refTownStateId: Optional[int] = Query(None, description='Id Населенного пункта', schema={'type': 'integer', 'title': 'refTownStateId', 'description': 'Id Населенного пункта', 'examples': [1]}, title='refTownStateId', examples=[1]),
	refVendorModelId: Optional[int] = Query(None, description='Ид модели ЦАТС/SWW', schema={'type': 'integer', 'title': 'refVendorModelId', 'description': 'Ид модели ЦАТС/SWW', 'examples': [1]}, title='refVendorModelId', examples=[1]),
) -> Union[PhoneActivateSearchListResponse, BaseResponse]:
    """
    Get Phone Activation Request List
    """
    pass
    

    
@app.get(
    '/api/phone-activate-be/v1.0/get-request-list-cnt', 
    response_model=CountModel, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод для поиска в GUI, Организации постраничности')
async def get_phone_activation_request_list_cnt_api_phone_activate_be_v1_0_get_request_list_cnt_get(
	filialId: Optional[int] = Query(None, description='Ид филиала', schema={'type': 'integer', 'title': 'filialId', 'description': 'Ид филиала', 'examples': [5]}, title='filialId', examples=[5]),
	entityId: Optional[int] = Query(None, description='Ид сущности', schema={'type': 'integer', 'title': 'entityId', 'description': 'Ид сущности', 'examples': [22]}, title='entityId', examples=[22]),
	entitySpecId: Optional[int] = Query(None, description='Ид спец сущности entitySpecId', schema={'type': 'integer', 'title': 'entitySpecId', 'description': 'Ид спец сущности entitySpecId', 'examples': [10222221]}, title='entitySpecId', examples=[10222221]),
	customerAccountId: Optional[int] = Query(None, description='Ид лицевого счета', schema={'type': 'integer', 'title': 'entitySpecId', 'description': 'Ид лицевого счета', 'examples': [1022222]}, title='entitySpecId', examples=[1022222]),
	shortNumber: Optional[constr(max_length=50)] = Query(None, description='Короткий номер Телефона', schema={'type': 'string', 'title': 'shortNumber', 'description': 'Короткий номер Телефона', 'maxLength': 50, 'examples': ['22654']}, title='shortNumber', examples=['22654']),
	insertDateFrom: Optional[datetime] = Query(None, description='Дата создания активации с', schema={'type': 'string', 'title': 'insertDateFrom', 'description': 'Дата создания активации с', 'format': 'date-time'}, title='insertDateFrom', format='date-time'),
	insertDateTo: Optional[datetime] = Query(None, description='Дата создания активации по', schema={'type': 'string', 'title': 'insertDateTo', 'description': 'Дата создания активации по', 'format': 'date-time'}, title='insertDateTo', format='date-time'),
	stateId: Optional[int] = Query(None, description='Ид stateId', schema={'type': 'integer', 'title': 'stateId', 'description': 'Ид stateId', 'examples': [1]}, title='stateId', examples=[1]),
	userLogin: Optional[str] = Query(None, description='Логин пользователя', schema={'type': 'string', 'title': 'userLogin', 'description': 'Логин пользователя', 'examples': ['alma-tech']}, title='userLogin', examples=['alma-tech']),
	isFallout: IsFalloutType = Query(None, description='1 - Показать ручные, 0- автоматические, Пусто/null все записи', schema={'title': 'isFallout', 'description': '1 - Показать ручные, 0- автоматические, Пусто/null все записи', 'examples': ['0,1'], 'allOf': [{'$ref': '#/components/schemas/isFalloutType'}]}, title='isFallout', examples=['0,1']),
	refExchangeIdList: Optional[str] = Query(None, description='refExchangeIdList список станций', schema={'type': 'string', 'title': 'refExchangeIdList', 'description': 'refExchangeIdList список станций', 'examples': ['1,2,33,44']}, title='refExchangeIdList', examples=['1,2,33,44']),
	refTownStateId: Optional[int] = Query(None, description='Id Населенного пункта', schema={'type': 'integer', 'title': 'refTownStateId', 'description': 'Id Населенного пункта', 'examples': [1]}, title='refTownStateId', examples=[1]),
	refVendorModelId: Optional[int] = Query(None, description='Ид модели ЦАТС/SWW', schema={'type': 'integer', 'title': 'refVendorModelId', 'description': 'Ид модели ЦАТС/SWW', 'examples': [1]}, title='refVendorModelId', examples=[1]),
) -> Union[BaseResponse, CountModel]:
    """
    Get Phone Activation Request List Cnt
    """
    pass
    

    
@app.get(
    '/api/phone-activate-be/v1.0/get-history', 
    response_model=PhoneActivateHistoryListResponse, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод для поиска в GUI. Вкладка история изменений')
async def get_phone_activation_history_api_phone_activate_be_v1_0_get_history_get(
	phoneActivateId: conint(ge=0) = Query(..., description='Ид заявки на активацию', schema={'type': 'integer', 'title': 'phoneActivateId', 'description': 'Ид заявки на активацию', 'minimum': 0, 'examples': [10]}, title='phoneActivateId', examples=[10]),
) -> Union[BaseResponse, PhoneActivateHistoryListResponse]:
    """
    Get Phone Activation History
    """
    pass
    

    
@app.get(
    '/api/phone-activate-be/v1.0/get-reject-reason', 
    response_model=RejectReasonList, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод для выбора актуальных причин отказа')
async def get_reject_reason_api_phone_activate_be_v1_0_get_reject_reason_get(
) -> Union[RejectReasonList, BaseResponse]:
    """
    Get Reject Reason
    """
    pass
    

    
@app.get(
    '/api/phone-activate-be/v1.0/get-ref-town-state-list', 
    response_model=RefTownStateList, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод  для фильтра в GUI. Список нас. пунктов')
async def get_ref_town_state_list_api_phone_activate_be_v1_0_get_ref_town_state_list_get(
	filialId: int = Query(..., description='Ид филиала', schema={'type': 'integer', 'title': 'filialId', 'description': 'Ид филиала', 'examples': [5]}, title='filialId', examples=[5]),
	insertDateFrom: Optional[datetime] = Query(None, description='Дата создания активации с. Подаем с формы вместо is_archive', schema={'type': 'string', 'title': 'insertDateFrom', 'description': 'Дата создания активации с. Подаем с формы вместо is_archive', 'format': 'date-time'}, title='insertDateFrom', format='date-time'),
	insertDateTo: Optional[datetime] = Query(None, description='Дата создания активации по Подаем с формы вместо is_archive', schema={'type': 'string', 'title': 'insertDateTo', 'description': 'Дата создания активации по Подаем с формы вместо is_archive', 'format': 'date-time'}, title='insertDateTo', format='date-time'),
	refExchangeIdList: Optional[str] = Query(None, description='refExchangeIdList список станций', schema={'type': 'string', 'title': 'refExchangeIdList', 'description': 'refExchangeIdList список станций', 'examples': ['1,2,33,44']}, title='refExchangeIdList', examples=['1,2,33,44']),
) -> Union[BaseResponse, RefTownStateList]:
    """
    Get Ref Town State List
    """
    pass
    

    
@app.get(
    '/api/phone-activate-be/v1.0/get-ref-vendor-model-list', 
    response_model=RefVendorModelList, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод  для фильтра в GUI. Список вендор-модели')
async def get_ref_vendor_model_list_api_phone_activate_be_v1_0_get_ref_vendor_model_list_get(
	filialId: int = Query(..., description='Ид филиала', schema={'type': 'integer', 'title': 'filialId', 'description': 'Ид филиала', 'examples': [5]}, title='filialId', examples=[5]),
	insertDateFrom: Optional[datetime] = Query(None, description='Дата создания активации с. Подаем с формы вместо is_archive', schema={'type': 'string', 'title': 'insertDateFrom', 'description': 'Дата создания активации с. Подаем с формы вместо is_archive', 'format': 'date-time'}, title='insertDateFrom', format='date-time'),
	insertDateTo: Optional[datetime] = Query(None, description='Дата создания активации по Подаем с формы вместо is_archive', schema={'type': 'string', 'title': 'insertDateTo', 'description': 'Дата создания активации по Подаем с формы вместо is_archive', 'format': 'date-time'}, title='insertDateTo', format='date-time'),
	refTownStateId: Optional[int] = Query(None, description='Id Населенного пункта', schema={'type': 'integer', 'title': 'refTownStateId', 'description': 'Id Населенного пункта', 'examples': ['61']}, title='refTownStateId', examples=['61']),
	refExchangeIdList: Optional[str] = Query(None, description='refExchangeIdList список станций', schema={'type': 'string', 'title': 'refExchangeIdList', 'description': 'refExchangeIdList список станций', 'examples': ['1,2,33,44']}, title='refExchangeIdList', examples=['1,2,33,44']),
) -> Union[BaseResponse, RefVendorModelList]:
    """
    Get Ref Vendor Model List
    """
    pass
    

    
@app.get(
    '/api/phone-activate-be/v1.0/get-ref-exchange-list', 
    response_model=RefExchangeListResponse, 
    tags=['GUI Flow'], 
    responses={'400': {'description': 'Bad Request', 'model': BaseResponse, }, '401': {'description': 'Unauthorized', 'model': BaseResponse, }, '403': {'description': 'Forbidden', 'model': BaseResponse, }, '404': {'description': 'Not Found', 'model': BaseResponse, }, '422': {'description': 'Unprocessable Entity', 'model': BaseResponse, }, '500': {'description': 'Internal Server Error', 'model': BaseResponse, }, '503': {'description': 'Service Unavailable', 'model': BaseResponse, }, },
    description='Метод для фильтра в GUI. Список станций')
async def get_ref_exchange_list_api_phone_activate_be_v1_0_get_ref_exchange_list_get(
	filialId: int = Query(..., description='Ид филиала', schema={'type': 'integer', 'title': 'filialId', 'description': 'Ид филиала', 'examples': [5]}, title='filialId', examples=[5]),
	insertDateFrom: Optional[datetime] = Query(None, description='Дата создания активации с. Подаем с формы вместо is_archive', schema={'type': 'string', 'title': 'insertDateFrom', 'description': 'Дата создания активации с. Подаем с формы вместо is_archive', 'format': 'date-time'}, title='insertDateFrom', format='date-time'),
	insertDateTo: Optional[datetime] = Query(None, description='Дата создания активации по Подаем с формы вместо is_archive', schema={'type': 'string', 'title': 'insertDateTo', 'description': 'Дата создания активации по Подаем с формы вместо is_archive', 'format': 'date-time'}, title='insertDateTo', format='date-time'),
	refTownStateId: Optional[int] = Query(None, description='Id Населенного пункта', schema={'type': 'integer', 'title': 'refTownStateId', 'description': 'Id Населенного пункта', 'examples': ['1,']}, title='refTownStateId', examples=['1,']),
	refVendorModelId: Optional[int] = Query(None, description='Ид модели ЦАТС/SWW', schema={'type': 'integer', 'title': 'refVendorModelId', 'description': 'Ид модели ЦАТС/SWW', 'examples': ['61']}, title='refVendorModelId', examples=['61']),
	refExchangeIdList: Optional[str] = Query(None, description='refExchangeIdList список станций', schema={'type': 'string', 'title': 'refExchangeIdList', 'description': 'refExchangeIdList список станций', 'examples': ['1,2,33,44']}, title='refExchangeIdList', examples=['1,2,33,44']),
) -> Union[RefExchangeListResponse, BaseResponse]:
    """
    Get Ref Exchange List
    """
    pass
    


openapi_schema = get_openapi(title='phone-activate-be', version='1.0', 
    description='Микросервис активации Телефонии на ЦАТС/SWW в ручном или автоматическом режиме.', contact=contact_info, routes=app.routes)

openapi_schema['openapi'] = '3.1.0'
openapi_schema['servers'] = servers_info

with open('generated_api.yaml', 'w', encoding='utf-8') as output_file:
    yaml.dump(openapi_schema, output_file, allow_unicode=True)
