from abc import ABC, abstractmethod
import uuid

from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception

"""
Абстрактный класс для наследования моделей данных
"""


class abstract_reference(ABC):
    __name: str = ""
    __max_name: int = 50


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise argument_exception()

        if len(value) > self.__max_name:
            raise length_exception(max_len=self.__max_name, argument_name="name")

        self.__name = value