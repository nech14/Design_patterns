from modules.exceptions.abstract_logic import abstract_logic


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
    def data(self) :
        return self.__data


    @staticmethod
    def nomenclature_key() -> str:
        return "nomenclature"


    @staticmethod
    def range_key() -> str:
        return "range"


    @staticmethod
    def receipt_key() -> str:
        return "receipt"


    """
    Ключ для хранения групп номенклатуры
    """
    @staticmethod
    def group_key() -> str:
        return "group"
    
    """
    Перегрузка абстрактного метода
    """
    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)    
    

    

