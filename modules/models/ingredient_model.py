from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_model import nomenclature_model


class ingredient_model(nomenclature_model):
    __value = 0
    __nomenclature_code: nomenclature_model

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        argument_exception.isinstance(value, int)

        self.__value= value

    @property
    def nomenclature_code(self):
        return self.__nomenclature_code

    @nomenclature_code.setter
    def nomenclature_code(self, value: nomenclature_model):
        argument_exception.isinstance(value, nomenclature_model)

        self.__nomenclature_code = value