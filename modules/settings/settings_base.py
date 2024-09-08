"""
Настройки
"""


class Settings:
    __organization_name = ""
    __inn = ""
    __correspondent_account = ""
    __BIC = ""
    __type_of_property = ""
    __score = ""

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
            raise TypeError("Некорректно передан параметр!")

        self.__organization_name = value


    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно переданы параметры!")

        if not value.isdigit():
            raise TypeError("Должен быть только из цифр!")

        if len(value) != self.__inn_size:
            raise TypeError(f"Должен быть из {self.__inn_size} цифр!")

        self.__inn = value



    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value:str):
        if not isinstance(value, str):
            raise TypeError("Некорректно переданы параметры!")

        if len(value) != self.__correspondent_account_size:
            raise TypeError(f"Должен быть из {self.__correspondent_account_size} символов!")

        self.__correspondent_account = value



    @property
    def BIC(self):
        return self.__BIC

    @BIC.setter
    def BIC(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно переданы параметры!")

        if len(value) != self.__BIC_size:
            raise TypeError(f"Должен быть из {self.__BIC_size} символов!")

        self.__BIC = value



    @property
    def type_of_property(self):
        return self.__type_of_property

    @type_of_property.setter
    def type_of_property(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно переданы параметры!")

        if len(value) != self.__type_of_property_size:
            raise TypeError(f"Должен быть из {self.__type_of_property_size} символов!")

        self.__type_of_property = value


    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно переданы параметры!")

        if len(value) != self.__score_size:
            raise TypeError(f"Должен быть из {self.__score_size} символов!")

        self.__score = value