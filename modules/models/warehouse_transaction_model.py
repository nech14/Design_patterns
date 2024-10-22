from datetime import datetime

from modules.Enums.transaction_type import transaction_type
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.warehouse_model import warehouse_model


class warehouse_transaction_model(abstract_model):

    __warehouse: warehouse_model = None
    __nomenclature: nomenclature_model = None
    __quantity: int = None
    __transaction_type: transaction_type = None
    __range: range_model = None
    __period: datetime = None

    @property
    def warehouse(self):
        return self.__warehouse

    @warehouse.setter
    def warehouse(self, value: warehouse_model):
        argument_exception.isinstance(value, warehouse_model)

        self.__warehouse = value

    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        argument_exception.isinstance(value, nomenclature_model)

        self.__nomenclature = value


    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        argument_exception.isinstance(value, int)
        argument_exception.notIsinstance(value, bool, int)

        self.__quantity = value


    @property
    def transaction_type(self):
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value: transaction_type):
        argument_exception.isinstance(value, transaction_type)

        self.__transaction_type = value


    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value: range_model):
        argument_exception.isinstance(value, range_model)

        self.__range = value


    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, value: datetime):
        argument_exception.isinstance(value, datetime)

        self.__period = value