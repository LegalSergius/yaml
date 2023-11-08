from pydantic import Field, BaseModel


class BuildingGeoCords200ResponseData(BaseModel):
    
    """
    Данные ответа
    """
    

    pointLon: str = Field(..., description='Долгота')

    pointLat: str = Field(..., description='Широта')
