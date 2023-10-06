from pydantic import BaseModel, Field
from . import BuildingGeoCordsResponseData


class BuildingGeoCordsResponse(BaseModel):
    

    
    data: BuildingGeoCordsResponseData = Field(..., description='Данные ответа')
    
    
    
