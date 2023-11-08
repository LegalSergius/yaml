from pydantic import conint, BaseModel, Field, constr
from typing import Optional


class PhoneManualExecuteRequest(BaseModel):
    

    phoneActivateId: conint(ge=0) = Field(..., title='phoneActivateId', description='Ид заявки на активацию ', examples=[101])

    feRejectReasonId: Optional[int] = Field(..., title='feRejectReasonId', description='Идентификатор причины отказа', examples=[0])

    resultId: int = Field(..., title='resultId', description='Идентификатор результата', examples=[0])

    userLogin: constr(max_length=255) = Field(..., title='userLogin', description='Пользователь который назначает ', examples=['alm-tech'])

    fxsLogin: Optional[constr(max_length=255)] = Field(None, title='fxsLogin', description='Логин FXS ', examples=['7278900108'])

    fxsPwd: Optional[constr(max_length=255)] = Field(None, title='fxsPwd', description='Пароль FXS ', examples=['!@312421412'])

    message: Optional[constr(max_length=4000)] = Field(None, title='message', description='Примечание, если есть ошибка ', examples=['Комментарий'])
