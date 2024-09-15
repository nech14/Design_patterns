from abc import ABC, abstractmethod
import uuid

from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception

"""
Абстрактный класс для наследования моделей данных
"""


class abstract_model(ABC):
    __name: str = ""
    __max_name: int = 50
    __unique_code:str =  uuid.uuid4()


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

    """
      Уникальный код
      """

    @property
    def unique_code(self) -> str:
        return self.__unique_code


    @unique_code.setter
    def unique_code(self, value: str):
        if not isinstance(value, str):
            raise argument_exception()
        self.__unique_code = value

    """
    Вариант сравнения (по коду)
    """

    @abstractmethod
    def set_compare_mode(self, other_object) -> bool:
        if other_object is None: return False
        if not isinstance(other_object, abstract_model): return False

        return self.__unique_code == other_object.unique_code

    def __eq__(self, value: object) -> bool:
        return self.set_compare_mode(value)