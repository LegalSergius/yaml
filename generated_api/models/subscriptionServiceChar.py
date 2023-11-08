from pydantic import BaseModel, Field, constr


class SubscriptionServiceChar(BaseModel):
    

    charName: constr(max_length=255) = Field(..., title='charName', description='Имя хар-ки', examples=['Номер для переадресации (с маской в формате телефонного номера)'])

    charValue: constr(max_length=4000) = Field(..., title='charValue', description='Значение хар-ки', examples=['3'])
