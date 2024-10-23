from abc import ABC, abstractmethod
import uuid
from datetime import datetime
from enum import Enum

from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception
"""
Абстрактный класс для наследования моделей данных
"""


class abstract_model(ABC):
    __name: str = ""
    __max_name: int = 50
    __unique_code:str = None

    @classmethod
    def assign_model_unique_code(cls):
        if cls.__unique_code is None:
            cls.__unique_code = str(uuid.uuid4())  # Уникальный код для каждого класса


    def __init__(self):
        self.__name = ""
        # self.assign_model_unique_code()
        # self.__model_unique_code = self.__class__.__model_unique_code
        self.__unique_code = str(uuid.uuid4())

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
    def unique_code(self):
        return self.__unique_code


    @unique_code.setter
    def unique_code(self, value: str):
        if not isinstance(value, str):
            raise argument_exception()
        self.__unique_code = value

    """
    Вариант сравнения (по коду)
    """


    def set_compare_mode(self, other_object) -> bool:
        if other_object is None: return False
        if not isinstance(other_object, abstract_model): return False

        return self.__unique_code == other_object.unique_code

    def __eq__(self, value: 'abstract_model') -> bool:
        return self.set_compare_mode(value)


    """
    Преобразование класса в словарь
    """

    def get_dict(self):

        # Рекурсивная функция для преобразования атрибутов в словарь
        def recursive_to_dict(value):

            if isinstance(value, Enum):
                return {f"{value.__class__.__name__}": value.name}
            elif hasattr(value, '__dict__'):  # Пользовательский класс
                class_name = value.__class__.__name__

                return {'__class__': class_name, **{self._normalize_key(key): recursive_to_dict(getattr(value, key))
                                                    for key in vars(value)}}
            elif isinstance(value, list):
                return [recursive_to_dict(item) for item in value]
            elif isinstance(value, dict):
                return {k: recursive_to_dict(v) for k, v in value.items()}
            else:
                return value

        return {'__class__': self.__class__.__name__,
                **{self._normalize_key(key): recursive_to_dict(value) for key, value in vars(self).items()}}
        # return {self._normalize_key(key): recursive_to_dict(value) for key, value in vars(self).items()}

    def _normalize_key(self, key):
        # Убираем имя класса из "name mangled" атрибутов, если они есть
        if key.startswith('_'):
            parts = key.split('__', 1)  # Разбиваем по двойному подчёркиванию
            if len(parts) > 1:
                return parts[1]  # Возвращаем только часть без имени класса
        return key  # Если не приватный атрибут, возвращаем как есть


    def __str__(self):
        # Для удобства вывода преобразуем словарь в строку
        return str(self.get_dict())

    """
    Проверка реализован ли метод у класса, а не у родителя
    """

    def is_method_defined_in_child(self, method_name):
        # Получаем метод из текущего класса
        method = getattr(self, method_name, None)
        # Проверяем, что метод существует и он определён в текущем классе
        return method is not None and method.__qualname__.startswith(self.__class__.__name__)


    def __repr__(self):
        return self.__str__()

