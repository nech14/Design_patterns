from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_reference import abstract_reference

class range_model(abstract_reference):
    __base_unit_measurement: 'range_model'
    __conversion_factor = 1

    def __init__(self, name, conversion_factor: int = 1, base_unit_measurement: 'range_model' = None):
        if (
                not isinstance(conversion_factor, int) or
                not (isinstance(base_unit_measurement, range_model) or base_unit_measurement is None) or
                not isinstance(name, str)
        ):
            raise argument_exception()

        self.__name = name
        self.__conversion_factor = conversion_factor
        self.__base_unit_measurement = base_unit_measurement


    @property
    def base_unit_measurement(self) -> 'range_model':
        return self.__base_unit_measurement


    @base_unit_measurement.setter
    def base_unit_measurement(self, value: 'range_model'):
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
