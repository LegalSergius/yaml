from typing import Optional
from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    

    errCode: Optional[int] = Field(0, title='Errcode', description='Код ошибки')

    errMsg: Optional[str] = Field(None, title='Errmsg', description='Текст ошибки')
