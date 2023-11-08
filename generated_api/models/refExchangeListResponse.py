from . import RefExchange
from typing import List, Optional
from pydantic import BaseModel, Field


class RefExchangeListResponse(BaseModel):
    

    refExchangeList: Optional[List[RefExchange]] = Field(None, title='Refexchangelist', description='Список станций', items={'$ref': '#/components/schemas/refExchange'})
