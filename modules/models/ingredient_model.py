from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_model import nomenclature_model


class ingredient_model(nomenclature_model):
    __value = 0

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        argument_exception.isinstance(value, int)

        self.__value= value