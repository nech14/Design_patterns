from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_model import nomenclature_model


class ingredient_model(nomenclature_model):
    __grams = 0

    @property
    def grams(self):
        return self.__grams

    @grams.setter
    def grams(self, value: int):
        argument_exception.isinstance(value, int)

        self.__grams = value