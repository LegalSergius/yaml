# generated by fastapi-codegen:
#   filename:  api.yaml
#   timestamp: 2023-09-27T16:49:51+00:00

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, Query
from fastapi.openapi.utils import get_openapi

from models import BuildingGeoCordsGetResponse, TraceCopper, TraceOptical

import yaml

app = FastAPI(
    title='vcip-api',
    version='1.0',
    description='Сервисы VCIP',
    contact={'name': 'Shakhmurat Japparov', 'email': 'japparov.s@telecom.kz'},
    servers=[{'url': 'http://localhost:3000/api/vcip-api/v1.0', 'description': 'test'}],
)


@app.get(
    '/building-geo-cords',
    response_model=BuildingGeoCordsGetResponse,
    tags=['Геокоординаты'],
)
def get_building_geo_cords(
    town_state_id: int = Query(..., alias='townStateId'),
    street_id: int = Query(..., alias='streetId'),
    building_num: int = Query(..., alias='buildingNum'),
    building_sub_num: Optional[str] = Query(None, alias='buildingSubNum'),
) -> BuildingGeoCordsGetResponse:
    """
    Получить геокоординаты здания
    """
    pass


@app.get(
    '/trace-copper', response_model=TraceCopper, tags=['Трассировка по медной сети']
)
def get_trace_copper(
    town_state_id: float = Query(..., alias='townStateId'),
    container_external_id: float = Query(..., alias='containerExternalId'),
    mounted_port_num: str = Query(..., alias='mountedPortNum'),
) -> TraceCopper:
    """
    Получить трассировку по медной сети
    """
    pass


@app.get(
    '/trace-optical',
    response_model=TraceOptical,
    tags=['Трассировка по оптической сети'],
)
def get_trace_optical(
    town_state_id: float = Query(..., alias='townStateId'),
    container_spec_id: float = Query(..., alias='containerSpecId'),
    container_external_id: float = Query(..., alias='containerExternalId'),
    mounted_port_num: str = Query(..., alias='mountedPortNum'),
) -> TraceOptical:
    """
    Получить трассировку по оптической сети
    """
    pass

openapi_schema = get_openapi(title='vcip-api', version='3.0.0', description='Сервисы VCIP', routes=app.routes,
                              servers=[{'url': 'http://localhost:3000/api/vcip-api/v1.0', 'description': 'test'}], contact={'name': 'Shakhmurat Japparov', 'email': 'japparov.s@telecom.kz'})

with open('generated_api.yaml', 'w', encoding='utf-8') as output_file:
    yaml.dump(openapi_schema, output_file)