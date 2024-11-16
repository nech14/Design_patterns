from datetime import datetime

from modules.Enums.transaction_type import enum_transaction_type
from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception
from modules.models.abstract_model import abstract_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.warehouse_model import warehouse_model


class warehouse_transaction_model(abstract_model):

    __warehouse: warehouse_model = None
    __nomenclature: nomenclature_model = None
    __range: range_model = None
    __transaction_type: enum_transaction_type = None
    __quantity: int = None
    __period: datetime = None


    @staticmethod
    def income_transaction(value1, value2):
        return value1 + value2

    @staticmethod
    def expense_transaction(value1, value2):
        return value1 - value2

    __operation_transaction = [income_transaction, expense_transaction]

    @staticmethod
    def operation_transaction(number:int):
        argument_exception.isinstance(number, int)
        if number <= 0 or number > len(warehouse_transaction_model.__operation_transaction):
            length_exception(len(warehouse_transaction_model.__operation_transaction))

        return warehouse_transaction_model.__operation_transaction[number-1]


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
    def transaction_type(self, value: enum_transaction_type):
        argument_exception.isinstance(value, enum_transaction_type)

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
    def period(self, value: datetime|str):
        argument_exception.isinstance(value, datetime|str)

        if isinstance(value, str):
            value = datetime.fromisoformat(value)

        self.__period = value


    @staticmethod
    def get_base_warehouse_transaction(
            name="test_warehouse_transaction",
            warehouse=warehouse_model.get_base_warehouse(),
            nomenclature=nomenclature_model(),
            quantity=1,
            transaction_type=enum_transaction_type.Income,
            range=range_model("test_range"),
            period=datetime.now()
    ):
        item_warehouse_transaction = warehouse_transaction_model()

        item_warehouse_transaction.name = name
        item_warehouse_transaction.warehouse = warehouse
        item_warehouse_transaction.nomenclature = nomenclature
        item_warehouse_transaction.quantity = quantity
        item_warehouse_transaction.transaction_type = transaction_type
        item_warehouse_transaction.range = range
        item_warehouse_transaction.period = period

        return item_warehouse_transaction