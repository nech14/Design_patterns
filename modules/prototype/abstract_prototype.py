from abc import ABC, abstractmethod

from modules.exceptions.argument_exception import argument_exception

"""
Абстрактный класс прототип
"""
class abstract_prototype(ABC):
    __data = []

    def __init__(self, source:list) -> None:
        super().__init__()
        argument_exception.isinstance(source, list)
        self.__data = source

    @abstractmethod
    def create(self, data:list, filter):
        argument_exception.isinstance(data, list)
        if filter is None:
            raise argument_exception("Некорректно указан параметр!")

    """
    Полученный набор данных
    """
    @property
    def data(self) -> list:
        return self.__data    
    
    @data.setter
    def data(self, value:list):
        self.__data = value

         