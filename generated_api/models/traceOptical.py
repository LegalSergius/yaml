from pydantic import BaseModel, Field
from . import TraceOpticalData


class TraceOptical(BaseModel):
    
    """
    Данные трассировки по оптической сети
    """
    

    
    data: TraceOpticalData = Field(..., description='Данные ответа')
    
    
    
