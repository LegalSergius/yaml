from . import RefTownState
from typing import List, Optional
from pydantic import BaseModel, Field


class RefTownStateList(BaseModel):
    

    refTownStateList: Optional[List[RefTownState]] = Field(None, title='Reftownstatelist', description='Список причин отказа', items={'$ref': '#/components/schemas/refTownState'})
