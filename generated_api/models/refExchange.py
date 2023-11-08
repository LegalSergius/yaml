from pydantic import BaseModel, Field, constr


class RefExchange(BaseModel):
    

    id: int = Field(..., title='phoneActivateId', description='Ид станции', examples=[101])

    name: constr(max_length=255) = Field(..., title='name', description='Наименование станции', examples=['Pavlodar Huawei'])
