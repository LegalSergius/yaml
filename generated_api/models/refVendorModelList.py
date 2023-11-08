from . import RefVendorModel
from typing import List, Optional
from pydantic import BaseModel, Field


class RefVendorModelList(BaseModel):
    

    refVendorModelList: Optional[List[RefVendorModel]] = Field(None, title='Refvendormodellist', description='Список моделий ЦАТС/SWW', items={'$ref': '#/components/schemas/refVendorModel'})
