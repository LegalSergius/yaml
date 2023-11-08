from . import TraceOpticalData
from pydantic import Field, BaseModel


class TraceOptical(BaseModel):
    
    """
    Данные трассировки по оптической сети
    """
    

    data: TraceOpticalData = Field(..., description='Данные ответа', properties={'lineData': {'type': 'string', 'description': 'Строка линейных данных', 'example': 'TOWN:727;STATION:40/01; MAN:ECI; OLT:3/00/06/06;ODF:2/08/09/06; LD:ОРШ 223/37: 00/00/1 магистраль/6, 00/00/2 сплиттеры /16, 00/00/2 сплиттеры /18, 00/00/5 распределение/12; ОРКсп 223/37/6/2: 00/00/1х16/11 (Этаж 5); OU:0;ONUPORTNUM:0; (DSL,SIP); 3.542 км'}})
