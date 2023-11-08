from pydantic import conint, BaseModel, Field, constr
from datetime import datetime
from typing import Optional


class PhoneAssignRequest(BaseModel):
    

    phoneActivateId: conint(ge=0) = Field(..., title='phoneActivateId', description='Ид заявки на активацию ', examples=[101])

    userLogin: constr(max_length=255) = Field(..., title='userLogin', description='Пользователь который назначает ', examples=['alm-tech'])

    userAssignLogin: constr(max_length=255) = Field(..., title='userAssignLogin', description='Пользователь кому назначена заявка ', examples=['alm-tech'])

    controlDate: Optional[datetime] = Field(None, title='controlDate', description='Дата контрольного срока', format='date-time')

    message: Optional[constr(max_length=4000)] = Field(None, title='message', description='Примечание, если есть ошибка ', examples=['Комментарий'])
