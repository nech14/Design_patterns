from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_model import nomenclature_model


class ingredient_model(nomenclature_model):
    __value = 0
    __nomenclature: nomenclature_model | None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        argument_exception.isinstance(value, int)

        self.__value= value

    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model|None):
        if value is None:
            return None

        argument_exception.isinstance(value, nomenclature_model)

        self.__nomenclature = value