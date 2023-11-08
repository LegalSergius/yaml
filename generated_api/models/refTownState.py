from pydantic import BaseModel, Field, constr


class RefTownState(BaseModel):
    

    id: int = Field(..., title='refTownStateId', description='Ид населенного пункта ', examples=[101])

    name: constr(max_length=255) = Field(..., title='name', description='Наименование населенного пункта  ', examples=['alm-tech'])
