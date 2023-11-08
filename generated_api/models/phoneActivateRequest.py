from pydantic import conint, BaseModel, Field, constr
from . import ActivatePhoneProcessTypeId, IsFalloutType, SubscriptionServiceChar, BaseCfsActionSpecIdTypeId, IsCanBeReactivatedType, PaSubscriptionService, PaOrderAdd_fs
from typing import List, Optional


class PhoneActivateRequest(BaseModel):
    

    entityId: conint(ge=0) = Field(..., title='entityId', description='Идентификатор сущности', examples=[6000021])

    entitySpecId: int = Field(..., title='entitySpecId', description='Идентификатор типа сущности', examples=[1, 22])

    processTypeId: ActivatePhoneProcessTypeId = Field(1, title='processTypeId', description='Тип процесса. 1 - Актвиация телефонии и ДВО/Деактивация телефонии и ДВО . 2-Откат актвиация телефонии и ДВО/Откат деактивация телефонии и ДВО', examples=[1, 2])

    callBackUrl: constr(max_length=255) = Field(..., title='callBackUrl', description='Ссылка на URL, ответа', examples=['http://osm'])

    createApplicationName: constr(max_length=255) = Field(..., title='createApplicationName', description='Приложение создатель ', examples=['OSM'])

    physicalResource: constr(max_length=50) = Field(..., title='physicalResource', description='Номер базового ресурса. FTTh,ETTh. Транспорт.', examples=['8034041'])

    shortNumber: constr(max_length=50) = Field(..., title='shortNumber', description='Короткий номер Телефона', examples=['22653'])

    oldFullNumber: Optional[constr(max_length=50)] = Field(None, title='shortNumber', description='Полный номер Телефона из VCIP', examples=['7277422652'])

    fullNumber: constr(max_length=50) = Field(..., title='fullNumber', description='Полный номер Телефона из VCIP', examples=['7277422653'])

    baseCfsActionSpecId: BaseCfsActionSpecIdTypeId = Field(..., title='baseCfsActionSpecId', description='Действие над базовым ресурсом, 1-Установка, 2-Изменение, 3-Снятие', examples=[1, 2, 3])

    baseCfsActionSpecName: constr(max_length=255) = Field(..., title='baseCfsActionSpecName', description='Наименование действия над базовым ресурсом', examples=['Установка'])

    addressLine: constr(max_length=255) = Field(..., title='addressLine', description='Строка адреса', examples=['г.Шымкент ул. ТУРКЕСТАНСКАЯ дом 11 кв. 0'])

    customerAccountId: int = Field(..., title='customerAccountId', description='Ид лицевого счета', examples=[1098881])

    customerAccountName: constr(max_length=255) = Field(..., title='customerAccountName', description='Наименование лицевого счета', examples=['РГП НА ПХВ"ИНЖЕНЕРНО-ТЕХНИЧЕСКИЙ ЦЕНТР ЦЕНТРАЛЬНОЙ...'])

    customerAccountNameKZ: Optional[constr(max_length=255)] = Field(None, title='customerAccountNameKZ', description='Наименование лицевого счета КЗ', examples=['РГП НА ПХВ"ИНЖЕНЕРНО-ТЕХНИЧЕСКИЙ ЦЕНТР ЦЕНТРАЛЬНОЙ...'])

    filialId: int = Field(..., title='filialId', description='Ид филиала', examples=[5])

    filialName: constr(max_length=100) = Field(..., title='filialName', description='Наименование филиала', examples=['Ю-К ОДТ'])

    paOrderAddСfsItems: Optional[List[PaOrderAdd_fs]] = Field(None, title='Paorderaddсfsitems', description='Массив команд для оборудования', items={'$ref': '#/components/schemas/paOrderAdd_fs'})

    paSubscriptionServiceItemsOld: Optional[List[PaSubscriptionService]] = Field(None, title='Pasubscriptionserviceitemsold', description='Текущий состав подписки. ДВО и Абон платы. При новом заказе пусто', items={'$ref': '#/components/schemas/paSubscriptionService'})

    paSubscriptionServiceItemsNew: Optional[List[PaSubscriptionService]] = Field(None, title='Pasubscriptionserviceitemsnew', description='Новый состав подписки. ДВО и Абон платы. При снятие пусто ', items={'$ref': '#/components/schemas/paSubscriptionService'})

    subscriptionServiceCharList: Optional[List[SubscriptionServiceChar]] = Field(None, title='subscriptionServiceCharList', description='Список хар-тик', items={'$ref': '#/components/schemas/subscriptionServiceChar'})

    priorityName: constr(max_length=100) = Field(..., title='priorityName', description='Наименование приоритета из заказа, категория абонента', examples=['Обычный'])

    refTownStateId: Optional[int] = Field(-1, title='refTownStateId', description='Id Населенного пункта', examples=[5])

    refTownStateName: Optional[constr(max_length=255)] = Field('Не определено', title='refTownStateName', description='Нас. пункт наименование', examples=[' г.Шымкент '])

    exchangeId: Optional[int] = Field(-1, title='exchangeId', description='Ид ЦАТС/SWW', examples=[5])

    exchangeName: Optional[constr(max_length=255)] = Field('Не определено', title='exchangeName', description='Наименование станции', examples=['Astana_GTS_SSW_CS2000'])

    refVendorModelId: Optional[int] = Field(-1, title='refVendorModelId', description='Id модели ЦАТС/SWW', examples=[100])

    refVendorModelName: Optional[constr(max_length=255)] = Field('Не определено', title='refVendorModelName', description='Наименование модели ЦАТС/SWW', examples=['Genband CS2000C'])

    adapterUrl: Optional[constr(max_length=512)] = Field(None, title='adapterUrl', description='adapterUrl - Ссылка для команд на станцию. REST API', examples=['http://10.8.26.66:7733/api/activate-resource-phone-adapter-be/v0.1/order'])

    isFallout: IsFalloutType = Field(..., title='isFallout', description='Если 1, то сразу на ручную работу заказ SWW/ЦАТС', examples=[0, 1])

    isCanBeReactivated: IsCanBeReactivatedType = Field(0, title='isCanBeReactivated', description='Если 1, дает возможность повторной активации', examples=[0, 1])

    message: Optional[constr(max_length=4000)] = Field(None, title='message', description='Примечание, если есть ошибка ', examples=['Не указаны cramer_switch_container_id/ssw_cust_group_id для global_number=7184090512 error_message=None local_number=90512 ssw_cust_group_id=None cramer_switch_container_id=None pool_id=140749 pool_name=90512-90512 service_type_id=18 base_resource_spec_id=1005005 ref_town_state_id=10608 status=used в ответе сервиса VCIP.'])

    positionId: Optional[str] = Field(..., title='positionId', description='Идентификатор позиции', examples=[1808077001])
