from pydantic import conint, BaseModel, Field, constr
from typing import Optional


class PhoneRepeatAutoRequest(BaseModel):
    

    phoneActivateId: conint(ge=0) = Field(..., title='phoneActivateId', description='Ид заявки на активацию ', examples=[101])

    message: Optional[constr(max_length=4000)] = Field(None, title='message', description='Примечание, если есть ошибка ', examples=['Комментарий'])
