from typing import Optional
from pydantic import Field, BaseModel


class TraceCopper(BaseModel):
    
    """
    Данные трассировки по медной сети
    """
    

    townStateId: Optional[int] = Field(None, example=2, description='Населенный пункт_ID')

    parentContainerExternalId: Optional[int] = Field(None, example=13, description='ID родительского физического контейнера во внешней системе')
