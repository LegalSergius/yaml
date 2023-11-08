from pydantic import BaseModel, Field, constr
from typing import List, Optional
from . import PaSwwCatsAddCfs, IsCanBeReactivatedType


class PhoneAutomatiSetFalloutRequest(BaseModel):
    

    phoneActivateId: int = Field(..., title='phoneActivateId', description='Ид заявки на активацию ', examples=[101])

    fxsLogin: Optional[constr(max_length=255)] = Field(None, title='fxsLogin', description='Логин FXS, в этом методе не обязательный ', examples=['7278900108'])

    fxsPwd: Optional[constr(max_length=255)] = Field(None, title='fxsPwd', description='Пароль FXS ', examples=['!@312421412'])

    paSwwCatsAddCfsItems: Optional[List[PaSwwCatsAddCfs]] = Field(None, title='Paswwcatsaddcfsitems', description='Точный набор ДВО на оборудовании', items={'$ref': '#/components/schemas/paSwwCatsAddCfs'})

    isCanBeReactivated: IsCanBeReactivatedType = Field(..., title='isCanBeReactivated', description='Если 1, дает возможность повторной активации', examples=[0, 1])

    message: Optional[constr(max_length=4000)] = Field(None, title='message', description='Текст ошибки от BPM Активации телефонии', examples=['Текст ошибки от BPM Активации телефонии'])
