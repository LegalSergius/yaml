from . import PhoneActivateSearch
from typing import List
from pydantic import BaseModel, Field


class PhoneActivateSearchListResponse(BaseModel):
    

    phoneActivateSearchListResponse: List[PhoneActivateSearch] = Field(..., title='Phoneactivatesearchlistresponse', description='Ответ для формы поиска', items={'$ref': '#/components/schemas/phoneActivateSearch'})
