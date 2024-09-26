from abc import ABC, abstractmethod

from modules.exceptions.argument_exception import argument_exception
from modules.reports.format_reporting import format_reporting


"""
Абстрактный класс для наследования для отчетов
"""
class abstract_report(ABC):
    __format: format_reporting = format_reporting.CSV
    __result:str = ""

    def __init__(self):
        pass

    """
    Сформировать
    """
    @abstractmethod
    def create(self, data: list):
        pass


    """
    Тип формата
    """
    @property
    def format(self) -> format_reporting:
        return self.__format


    @format.setter
    def format(self, value):
        self.__format = value
    
    """
    Результат формирования отчета
    """
    @property
    def result(self) -> str:
        return self.__result
    
    @result.setter
    def result(self, value:str):
        argument_exception.isinstance(value, str)
        self.__result = value
