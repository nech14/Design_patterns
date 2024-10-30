"""
Настройки
"""
from datetime import datetime

from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.base_exception import base_exeption
from modules.exceptions.length_exception import length_exception


class Settings:
    __organization_name = ""
    __inn = ""
    __correspondent_account = ""
    __BIC = ""
    __type_of_property = ""
    __score = ""
    __block_period: datetime

    __inn_size = 12
    __score_size = 11
    __correspondent_account_size = 11
    __BIC_size = 9
    __type_of_property_size = 5


    def __str__(self):
        return f"""
        Наименование организации = "{self.__organization_name}"
        ИНН = {self.__inn}
        Корреспондентский счет = {self.__correspondent_account}
        БИК = {self.__BIC}
        Вид собственности = {self.__type_of_property}
        Счет = {self.__score}
        """



    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        if not isinstance(value, str):
            raise argument_exception()
            # raise TypeError("Некорректно передан параметр!")

        self.__organization_name = value


    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise argument_exception()

        if not value.isdigit():
            raise argument_exception(message="Must be made up of numbers only!")

        if len(value) != self.__inn_size:
            raise length_exception(max_len=self.__inn_size, argument_name="inn")

        self.__inn = value



    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value:str):
        if not isinstance(value, str):
            raise argument_exception()

        if len(value) != self.__correspondent_account_size:
            raise length_exception(max_len=self.__correspondent_account_size, argument_name="correspondent_account")

        self.__correspondent_account = value



    @property
    def BIC(self):
        return self.__BIC

    @BIC.setter
    def BIC(self, value: str):
        if not isinstance(value, str):
            raise argument_exception()

        if len(value) != self.__BIC_size:
            raise length_exception(max_len=self.__BIC_size, argument_name="BIC")

        self.__BIC = value



    @property
    def type_of_property(self):
        return self.__type_of_property

    @type_of_property.setter
    def type_of_property(self, value: str):
        if not isinstance(value, str):
            raise argument_exception()

        if len(value) != self.__type_of_property_size:
            raise length_exception(max_len=self.__type_of_property_size, argument_name="type_of_property")

        self.__type_of_property = value


    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value: str):
        if not isinstance(value, str):
            raise argument_exception()

        if len(value) != self.__score_size:
            raise length_exception(max_len=self.__score_size, argument_name="score")

        self.__score = value

    @property
    def block_period(self) -> datetime:
        return self.__block_period

    @block_period.setter
    def block_period(self, value: datetime):
        if isinstance(value, str):
            try:
                self.__block_period = datetime.strptime(value, "%Y-%m-%d")
            except Exception as e:
                raise argument_exception(message=f"{e}")
        else:
            argument_exception.isinstance(value, datetime)

            self.__block_period = value

