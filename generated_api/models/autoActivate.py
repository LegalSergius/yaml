from pydantic import conint, BaseModel, Field, constr
from . import BaseCfsActionSpecIdTypeId, PaOrderAdd_fs
from typing import List, Optional


class AutoActivate(BaseModel):
    

    phoneActivateId: conint(ge=0) = Field(..., title='phoneActivateId', description='Ид заявки на активацию ', examples=[101])

    fullNumber: constr(max_length=50) = Field(..., title='fullNumber', description='Полный номер Телефона из VCIP', examples=['7277422653'])

    exchangeId: int = Field(..., title='exchangeId', description='Ид ЦАТС/SWW', examples=[5])

    refVendorModelId: int = Field(..., title='refVendorModelId', description='Ид модели ЦАТС/SWW', examples=[100])

    adapterUrl: constr(max_length=512) = Field(..., title='adapterUrl', description='adapterUrl - Ссылка для команд на станцию. REST API', examples=['http://10.8.26.66:7733/api/activate-resource-phone-adapter-be/v0.1/order'])

    entityId: conint(ge=0) = Field(..., title='entityId', description='Идентификатор сущности', examples=[6000021])

    entitySpecId: int = Field(..., title='entitySpecId', description='Идентификатор типа сущности', examples=[1, 22])

    baseCfsActionSpecId: BaseCfsActionSpecIdTypeId = Field(..., title='baseCfsActionSpecId', description='Действие над базовым ресурсом, 1-Установка, 2-Изменение, 3-Снятие', examples=[1, 2, 3])

    paOrderAddCfsItems: Optional[List[PaOrderAdd_fs]] = Field(None, title='Paorderaddcfsitems', description='Массив команд на оборудовании. ДВО', items={'$ref': '#/components/schemas/paOrderAdd_fs'})
