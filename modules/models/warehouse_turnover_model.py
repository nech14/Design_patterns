from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.warehouse_model import warehouse_model


class warehouse_turnover_model(abstract_model):

    __warehouse: warehouse_model = None
    __turnover: int = 0
    __nomenclature: nomenclature_model = None
    __range: range_model = None


    @property
    def warehouse(self):
        return self.__warehouse

    @warehouse.setter
    def warehouse(self, value: warehouse_model):
        argument_exception.isinstance(value, warehouse_model)

        self.__warehouse = value


    @property
    def turnover(self):
        return self.__turnover

    @turnover.setter
    def turnover(self, value: int):
        argument_exception.isinstance(value, int)
        argument_exception.notIsinstance(value, bool, int)

        self.__turnover = value


    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        argument_exception.isinstance(value, nomenclature_model)

        self.__nomenclature = value


    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value: range_model):
        argument_exception.isinstance(value, range_model)

        self.__range = value