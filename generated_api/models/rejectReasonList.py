from . import RejectReason
from typing import List, Optional
from pydantic import BaseModel, Field


class RejectReasonList(BaseModel):
    

    rejectReasonList: Optional[List[RejectReason]] = Field(None, title='Rejectreasonlist', description='Список причин отказа', items={'$ref': '#/components/schemas/rejectReason'})
