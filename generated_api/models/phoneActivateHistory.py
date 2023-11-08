from pydantic import conint, BaseModel, Field, constr
from typing import Optional
from datetime import datetime


class PhoneActivateHistory(BaseModel):
    

    phoneActivateId: conint(ge=0) = Field(..., title='phoneActivateId', description='Ид заявки на активацию  ', examples=[101])

    userLogin: Optional[constr(max_length=255)] = Field(None, title='userLogin', description='Пользователь кому назначена заявка ', examples=['alm-tech'])

    stateId: int = Field(..., title='stateId', description='Идентификатор статуса', examples=[0])

    stateName: constr(max_length=255) = Field(..., title='stateName', description='Наименование статуса', examples=['Новый'])

    insertDate: Optional[datetime] = Field(None, title='insertDate', description='Дата создания')

    comment: Optional[constr(max_length=4000)] = Field(..., title='comment', description='Примечание пользователя ', examples=['Выполнено вручную'])
