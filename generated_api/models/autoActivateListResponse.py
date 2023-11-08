from . import AutoActivate
from typing import List
from pydantic import BaseModel, Field


class AutoActivateListResponse(BaseModel):
    

    autoActivatetListResponse: List[AutoActivate] = Field(..., title='Autoactivatetlistresponse', description='Список заявок для обработки BPM', items={'$ref': '#/components/schemas/autoActivate'})
