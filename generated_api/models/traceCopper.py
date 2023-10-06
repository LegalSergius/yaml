from pydantic import BaseModel, Field
from typing import Optional


class TraceCopper(BaseModel):
    
    """
    Данные трассировки по медной сети
    """
    

    
    townStateId: Optional[int] = Field(None, description='Населенный пункт_ID', example=2)
    

    
    parentContainerExternalId: Optional[int] = Field(None, description='ID родительского физического контейнера во внешней системе', example=13)
    
