from fastapi import FastAPI, Query
from fastapi.openapi.utils import get_openapi
from typing import Optional
from models import *

import yaml


contact_info = {
    'name': 'Shakhmurat Japparov', 
    'email': 'japparov.s@telecom.kz'
}

servers_info = [

    {'url': 'http://localhost:3000/api/vcip-api/v1.0', 'description': 'test'},    

]

app = FastAPI()

    
@app.get('/trace-optical', response_model=TraceOptical, summary='Получить трассировку по оптической сети', tags=['Трассировка по оптической сети',], responses={'200': {'description': 'OK'}, '400': {'description': 'Bad Request'}, '404': {'description': 'Not Found'}, '408': {'description': 'Request Timeout'}, '500': {'description': 'Internal Server Error'}})
async def get_trace_optical(
	townStateId: float = Query(..., alias='townStateId', description='Населенный пункт_ID'),
	containerSpecId: float = Query(..., alias='containerSpecId', description='Спецификация физического контейнера_ID'),
	containerExternalId: float = Query(..., alias='containerExternalId', description='ID физического контейнера во внешней системе'),
	mountedPortNum: str = Query(..., alias='mountedPortNum', description='Номер монтированного порта'),
) -> TraceOptical:
    """
    Получить трассировку по оптической сети
    """
    pass
    

    
@app.get('/trace-copper', response_model=TraceCopper, summary='Получить трассировку по медной сети', tags=['Трассировка по медной сети',], responses={'200': {'description': 'OK'}})
async def get_trace_copper(
	townStateId: float = Query(..., alias='townStateId', description='Населенный пункт_ID'),
	containerExternalId: float = Query(..., alias='containerExternalId', description='ID физического контейнера во внешней системе'),
	mountedPortNum: str = Query(..., alias='mountedPortNum', description='Номер монтированного порта'),
) -> TraceCopper:
    """
    Получить трассировку по медной сети
    """
    pass
    

    
@app.get('/building-geo-cords', response_model=BuildingGeoCordsResponse, summary='Получить геокоординаты здания', tags=['Геокоординаты',], responses={'200': {'description': 'OK'}})
async def get_building_geo_cords(
	townStateId: int = Query(..., alias='townStateId', description='Населенный пункт_ID'),
	streetId: int = Query(..., alias='streetId', description='Улица_ID'),
	buildingNum: int = Query(..., alias='buildingNum', description='Номер здания'),
	buildingSubNum: Optional[str] = Query(None, alias='buildingSubNum', description='Дробь здания'),
) -> BuildingGeoCordsResponse:
    """
    Метод возвращает геокоординаты здания по параметрам
    """
    pass
    


openapi_schema = get_openapi(title='vcip-api', version='1.0', 
    description='Сервисы VCIP', contact=contact_info, routes=app.routes)

openapi_schema['openapi'] = '3.0.0'
openapi_schema['servers'] = servers_info

with open('generated_api.yaml', 'w', encoding='utf-8') as output_file:
    yaml.dump(openapi_schema, output_file, allow_unicode=True)