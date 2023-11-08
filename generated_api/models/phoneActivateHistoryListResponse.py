from . import PhoneActivateHistory
from typing import List
from pydantic import BaseModel, Field


class PhoneActivateHistoryListResponse(BaseModel):
    

    phoneActivateHistoryResponseList: List[PhoneActivateHistory] = Field(..., title='Phoneactivatehistoryresponselist', description='Ответ для формы поиска', items={'$ref': '#/components/schemas/phoneActivateHistory'})
