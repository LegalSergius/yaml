from pydantic import BaseModel, Field, constr


class RefVendorModel(BaseModel):
    

    id: int = Field(..., title='refVendorModelId', description='Ид модели ЦАТС/SWW', examples=[101])

    name: constr(max_length=255) = Field(..., title='name', description='Наименование модели ЦАТС/SWW ', examples=['alm-tech'])
