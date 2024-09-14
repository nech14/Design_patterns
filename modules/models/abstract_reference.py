from abc import ABC, abstractmethod
import uuid

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
            pass

        if len(value) > self.__max_name:
            pass

        self.__name = value