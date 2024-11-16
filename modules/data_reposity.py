from modules.Enums.data_key import data_key
from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception

"""
Репозиторий данных
"""
class data_reposity(abstract_logic):
    __data = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(data_reposity, cls).__new__(cls)
        return cls.instance 

    """
    Набор данных
    """
    @property
    def data(self) -> dict:
        return self.__data

    @data.setter
    def data(self, value: dict):
        argument_exception.isinstance(value, dict)

        self.data = value


    @staticmethod
    def nomenclature_key() -> str:
        return data_key.nomenclature_model.value


    @staticmethod
    def range_key() -> str:
        return data_key.range_model.value


    @staticmethod
    def receipt_key() -> str:
        return data_key.receipt_model.value


    @staticmethod
    def warehouse_key() -> str:
        return data_key.warehouse_model.value


    @staticmethod
    def warehouse_transaction_key() -> str:
        return data_key.warehouse_transaction_model.value


    """
    Ключ для хранения групп номенклатуры
    """
    @staticmethod
    def group_key() -> str:
        return data_key.nomenclature_group_model.value
    
    """
    Перегрузка абстрактного метода
    """
    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)    
    

    

