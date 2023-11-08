from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import datetime


class PaSwwCatsAddCfs(BaseModel):
    

    addCfsSpecName: constr(max_length=100) = Field(..., title='addCfsSpecName', description='Наименование ДВО или Абон. платы, получаем от адаптера', examples=['Услуги междугородной и международной связи'])

    addCfsSpecId: int = Field(..., title='addCfsSpecId', description='Действие над ДВО, получаем от адаптера', examples=[141, 142, 140])

    serviceTypeId: Optional[int] = Field(0, title='serviceTypeId', description='Ид типа сервиса, получаем от адаптера', examples=[1])

    updateDate: Optional[datetime] = Field(None, title='dateFrom', description='Дата вызова SWW/CATS')
