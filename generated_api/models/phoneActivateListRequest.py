from . import PhoneActivateRequest
from typing import List
from pydantic import BaseModel, Field


class PhoneActivateListRequest(BaseModel):
    

    phoneActivateList: List[PhoneActivateRequest] = Field(..., title='Phoneactivatelist', description='Массив данных Ключ/Значение', min_items=1, max_items=2, items={'$ref': '#/components/schemas/phoneActivateRequest'})
