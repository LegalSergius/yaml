from pydantic import BaseModel, Field, constr
from . import IsAutoType, AddCfsActionSpecTypeId
from datetime import datetime
from typing import Optional


class PaOrderAdd_fs(BaseModel):
    

    poElementId: int = Field(..., title='poElementId', description='Идентификатор элемента', examples=[1534886])

    poElementName: constr(max_length=255) = Field(..., title='callBackUrl', description='Наименование элемента', examples=['Услуги междугородной и международной связи'])

    addCfsActionSpecId: AddCfsActionSpecTypeId = Field(..., title='addCfsActionSpecId', description='Идентификатор действия над позицией 1 - Установка,3 - Снятие', examples=[1, 3])

    addCfsSpecName: constr(max_length=100) = Field(..., title='addCfsSpecName', description='Наименование ДВО или Абон. платы', examples=['Услуги междугородной и международной связи'])

    refCfsSpecId: int = Field(..., title='refCfsSpecId', description='Идентификатор ДВО', examples=[141, 142, 140])

    isAuto: IsAutoType = Field(..., title='isAuto', description='Признак автоматической активации, определется через конфигуратор', examples=[1, 0])

    serviceCount: int = Field(..., title='serviceCount', description='Кол-во элементов', examples=[1])

    dateFrom: Optional[datetime] = Field(None, title='dateFrom', description='Дата начала действия услуги')
