from pydantic import BaseModel, Field, constr


class RejectReason(BaseModel):
    

    id: int = Field(..., title='rejectReasonId', description='Ид причины отказа ', examples=[101])

    name: constr(max_length=255) = Field(..., title='userLogin', description='Наименование причины отказа', examples=['alm-tech'])

    nameKz: constr(max_length=255) = Field(..., title='userAssignLogin', description='Наименование причины отказа. На казахском языке', examples=['alm-tech'])
