from pydantic import BaseModel, Field


class CountModel(BaseModel):
    

    count: int = Field(..., title='count', description='Кол-во записей', examples=[0])
