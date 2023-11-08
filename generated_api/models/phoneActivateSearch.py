from pydantic import conint, BaseModel, Field, constr
from . import ActivatePhoneProcessTypeId, IsFalloutType, BaseCfsActionSpecIdTypeId
from typing import Optional
from datetime import datetime


class PhoneActivateSearch(BaseModel):
    

    phoneActivateId: conint(ge=0) = Field(..., title='phoneActivateId', description='Ид заявки на активацию ', examples=[101])

    entityId: conint(ge=0) = Field(..., title='entityId', description='Идентификатор сущности', examples=[6000021])

    entitySpecId: int = Field(..., title='entitySpecId', description='Идентификатор типа сущности', examples=[1, 22])

    processTypeId: ActivatePhoneProcessTypeId = Field(1, title='processTypeId', description='Тип процесса. 1 - Актвиация телефонии и ДВО/Деактивация телефонии и ДВО . 2-Откат актвиация телефонии и ДВО/Откат деактивация телефонии и ДВО', examples=[1, 2])

    stateId: int = Field(..., title='stateId', description='Идентификатор статуса', examples=[0])

    stateName: constr(max_length=100) = Field(..., title='stateName', description='Наименование статуса', examples=['Новый'])

    callBackUrl: constr(max_length=512) = Field(..., title='callBackUrl', description='Ссылка на URL, ответа', examples=['http://osm'])

    createApplicationName: constr(max_length=255) = Field(..., title='createApplicationName', description='Приложение создатель ', examples=['OSM'])

    updateApplicationName: Optional[constr(max_length=255)] = Field('', title='updateApplicationName', description='Приложение через которое обновили запрос', examples=['FE-PHONE'])

    insertDate: Optional[datetime] = Field(None, title='insertDate', description='Дата создания')

    updateDate: Optional[datetime] = Field(None, title='updateDate', description='Дата обновления')

    controlDate: Optional[datetime] = Field(None, title='controlDate', description='Контрольный срок. Не используется')

    assignDate: Optional[datetime] = Field(None, title='assignDate', description='Дата назначения')

    userLogin: Optional[constr(max_length=255)] = Field('', title='userLogin', description='Пользователь кому назначена заявка ', examples=['alm-tech'])

    resultId: Optional[int] = Field('', title='resultId', description='Идентификатор результата', examples=[0])

    physicalResource: constr(max_length=50) = Field(..., title='physicalResource', description='Номер базового ресурса. FTTh,ETTh. Транспорт.', examples=['8034041'])

    shortNumber: constr(max_length=50) = Field(..., title='shortNumber', description='Короткий номер Телефона', examples=['22653'])

    oldFullNumber: Optional[constr(max_length=50)] = Field(None, title='shortNumber', description='Полный номер Телефона из VCIP', examples=['7277422652'])

    fullNumber: constr(max_length=50) = Field(..., title='fullNumber', description='Полный номер Телефона из VCIP', examples=['7277422653'])

    baseCfsActionSpecId: BaseCfsActionSpecIdTypeId = Field(..., title='baseCfsActionSpecId', description='Действие над базовым ресурсом, 1-Установка, 2-Изменение, 3-Снятие', examples=[1, 2, 3])

    baseCfsActionSpecName: constr(max_length=255) = Field(..., title='baseCfsActionSpecName', description='Наименование действия над базовым ресурсом', examples=['Установка'])

    addressLine: Optional[constr(max_length=255)] = Field(None, title='addressLine', description='Строка адреса', examples=['г.Шымкент ул. ТУРКЕСТАНСКАЯ дом 11 кв. 0'])

    customerAccountId: int = Field(..., title='customerAccountId', description='Ид лицевого счета', examples=[1098881])

    customerAccountName: constr(max_length=255) = Field(..., title='customerAccountName', description='Наименование лицевого счета', examples=['РГП НА ПХВ"ИНЖЕНЕРНО-ТЕХНИЧЕСКИЙ ЦЕНТР ЦЕНТРАЛЬНОЙ...'])

    customerAccountNameKZ: Optional[constr(max_length=255)] = Field(None, title='customerAccountNameKZ', description='Наименование лицевого счета КЗ', examples=['РГП НА ПХВ"ИНЖЕНЕРНО-ТЕХНИЧЕСКИЙ ЦЕНТР ЦЕНТРАЛЬНОЙ...'])

    filialId: int = Field(..., title='filialId', description='Ид филиала', examples=[5])

    filialName: constr(max_length=100) = Field(..., title='filialName', description='Наименование филиала', examples=['Ю-К ОДТ'])

    priorityName: constr(max_length=100) = Field(..., title='priorityName', description='Наименование приоритета из заказа, категория абонента', examples=['Обычный'])

    refTownStateId: Optional[int] = Field(-1, title='refTownStateId', description='Id Населенного пункта', examples=[5])

    refTownStateName: Optional[constr(max_length=255)] = Field('Не определено', title='refTownStateName', description='Нас. пункт наименование', examples=[' г.Шымкент '])

    exchangeId: Optional[int] = Field(-1, title='exchangeId', description='Ид ЦАТС/SWW', examples=[5])

    exchangeName: Optional[constr(max_length=255)] = Field('Не определено', title='exchangeName', description='Наименование станции', examples=['Astana_GTS_SSW_CS2000'])

    refVendorModelId: Optional[int] = Field(-1, title='refVendorModelId', description='Ид модели ЦАТС/SWW', examples=[100])

    refVendorModelName: Optional[constr(max_length=255)] = Field('Не определено', title='refVendorModelName', description='Наименование модели ЦАТС/SWW', examples=['Genband CS2000C'])

    adapterUrl: Optional[constr(max_length=512)] = Field('Не определено', title='adapterUrl', description='adapterUrl - Ссылка для команд на станцию. REST API', examples=['http://10.8.26.66:7733/api/activate-resource-phone-adapter-be/v0.1/order'])

    isFallout: IsFalloutType = Field(0, title='isFallout', description='Если 1, то сразу на ручную работу заказ SWW/ЦАТС', examples=[0, 1])

    feRejectReasonId: Optional[int] = Field(..., title='feRejectReasonId', description='Идентификатор причины отказа', examples=[0])

    feRejectReasonName: Optional[constr(max_length=255)] = Field(None, title='feRejectReasonName', description='Наименование причины отказа ', examples=['Нет'])

    message: Optional[constr(max_length=4000)] = Field(None, title='message', description='Примечание, если есть ошибка ', examples=['Не указаны cramer_switch_container_id/ssw_cust_group_id для global_number=7184090512 error_message=None local_number=90512 ssw_cust_group_id=None cramer_switch_container_id=None pool_id=140749 pool_name=90512-90512 service_type_id=18 base_resource_spec_id=1005005 ref_town_state_id=10608 status=used в ответе сервиса VCIP.'])

    fxsLogin: Optional[constr(max_length=255)] = Field(None, title='fxsLogin', description='Логин FXS, в этом методе не обязательный ', examples=['7278900108'])

    fxsPwd: Optional[constr(max_length=255)] = Field(None, title='fxsPwd', description='Пароль FXS ', examples=['!@312421412'])
