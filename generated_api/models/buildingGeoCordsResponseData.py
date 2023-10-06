from pydantic import BaseModel, Field


class BuildingGeoCordsResponseData(BaseModel):
    
    """
    Данные ответа
    """
    

    
    pointLon: str = Field(..., description='Долгота')
    

    
    pointLat: str = Field(..., description='Широта')
    
