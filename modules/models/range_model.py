from modules.models.abstract_reference import abstract_reference

class range_model(abstract_reference):
    __base_unit_measurement: 'range_model'
    __conversion_factor = 1

    def __init__(self, name, conversion_factor: int = 1, base_unit_measurement: 'range_model' = None):
        if (
                not isinstance(base_unit_measurement, int) or
                not isinstance(base_unit_measurement, range_model) or
                not isinstance(name, str)
        ):
            pass

        self.__name = name
        self.__conversion_factor = conversion_factor
        self.__base_unit_measurement = base_unit_measurement


    @property
    def base_unit_measurement(self):
        return self.base_unit_measurement


    @base_unit_measurement.setter
    def base_unit_measurement(self, value: 'range_model'):
        if not isinstance(value, range_model):
            pass

        self.__base_unit_measurement = value


    @property
    def conversion_factor(self):
        return self.__conversion_factor


    @conversion_factor.setter
    def conversion_factor(self, value: str):
        if not isinstance(value, str):
            pass

        self.__conversion_factor = value
