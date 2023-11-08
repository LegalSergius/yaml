from . import BuildingGeoCords200ResponseData
from pydantic import Field, BaseModel


class BuildingGeoCords200Response(BaseModel):
    

    data: BuildingGeoCords200ResponseData = Field(..., description='Данные ответа', properties={'pointLon': {'type': 'string', 'description': 'Долгота'}, 'pointLat': {'type': 'string', 'description': 'Широта'}})
