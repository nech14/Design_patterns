from copy import copy

from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model

class range_model(abstract_model):
    __base_unit_measurement: 'range_model' = None
    __conversion_factor = 1
    __instance_model: list['range_model'] = []

    def __init__(self, name, conversion_factor: int = 1, base_unit_measurement: 'range_model' = None):
        if (
                not isinstance(conversion_factor, int) or
                not (isinstance(base_unit_measurement, range_model) or base_unit_measurement is None) or
                not isinstance(name, str)
        ):
            raise argument_exception()

        super().__init__()
        self.name = name
        self.__conversion_factor = conversion_factor
        self.__base_unit_measurement = base_unit_measurement


    @property
    def base_unit_measurement(self) -> 'range_model':
        return self.__base_unit_measurement


    @base_unit_measurement.setter
    def base_unit_measurement(self, value: 'range_model'):
        if value is None:
            self.__base_unit_measurement = None
            return
        if not isinstance(value, range_model):
            raise argument_exception()

        self.__base_unit_measurement = value


    @property
    def conversion_factor(self):
        return self.__conversion_factor


    @conversion_factor.setter
    def conversion_factor(self, value: int):
        if not isinstance(value, int):
            raise argument_exception()

        self.__conversion_factor = value


    def set_compare_mode(self, other_object: 'range_model') -> bool:
        if other_object is None: return False
        if not isinstance(other_object, range_model):
            raise argument_exception()

        return self.name == other_object.name


    @staticmethod
    def default_range_grams():
        range_instance = range_model("гр", 1)

        if not range_instance in range_model.__instance_model:
            range_model.__instance_model.append(range_instance)

        return copy(range_model.__instance_model[range_model.__instance_model.index(range_instance)])

    @staticmethod
    def default_range_kilogram():
        range_instance = range_model("кг", 1000, range_model.default_range_grams())

        if not range_instance in range_model.__instance_model:
            range_model.__instance_model.append(range_instance)

        return copy(range_model.__instance_model[range_model.__instance_model.index(range_instance)])


    @staticmethod
    def default_range_pieces():
        range_instance = range_model("шт", 1)

        if not range_instance in range_model.__instance_model:
            range_model.__instance_model.append(range_instance)

        return copy(range_model.__instance_model[range_model.__instance_model.index(range_instance)])


    def __eq__(self, value: 'range_model') -> bool:
        return self.name == value.name