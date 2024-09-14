from modules.models.abstract_reference import abstract_reference
from modules.settings.settings_base import Settings

class organization_model(abstract_reference):

    __INN = ""
    __BIC = ""
    __score = ""
    __form_ownership = ""


    def __init__(self, setting: Settings):
        if not isinstance(setting, Settings):
            pass

        self.__INN = setting.inn
        self.__BIC = setting.BIC
        self.__score = setting.score
        # self.__form_ownership = setting.type_of_property #форма собственности и вид собственности это одно и тоже?


    @property
    def INN(self):
        return self.__INN


    @INN.setter
    def INN(self, value: Settings):
        if not isinstance(value, Settings):
            pass

        self.__INN = value.inn


    @property
    def BIC(self):
        return self.__BIC


    @BIC.setter
    def BIC(self, value: Settings):
        if not isinstance(value, Settings):
            pass

        self.__BIC = value.BIC


    @property
    def score(self):
        return self.__score


    @score.setter
    def score(self, value: Settings):
        if not isinstance(value, Settings):
            pass

        self.__score = value.score


    @property
    def form_ownership(self):
        return self.__form_ownership


    @form_ownership.setter
    def form_ownership(self, value: str):
        if not isinstance(value, str):
            pass

        self.__form_ownership = value

