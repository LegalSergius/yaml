from pydantic import conint, BaseModel, Field, constr


class PhoneChangeFxsLoginPwd(BaseModel):
    

    phoneActivateId: conint(ge=0) = Field(..., title='phoneActivateId', description='Ид заявки на активацию ', examples=[101])

    userLogin: constr(max_length=255) = Field(..., title='userLogin', description='Пользователь который назначает ', examples=['alm-tech'])

    fxsLogin: constr(min_length=1, max_length=255) = Field(..., title='fxsLogin', description='Логин FXS, в этом методе не обязательный ', examples=['7278900108'])

    fxsPwd: constr(min_length=1, max_length=255) = Field(..., title='fxsPwd', description='Пароль FXS ', examples=['!@312421412'])
