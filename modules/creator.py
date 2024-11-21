from enum import Enum

from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model

from modules.models.range_model import range_model
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.ingredient_model import ingredient_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.receipt.receipt_model import receipt_model
from modules.models.warehouse_turnover_model import warehouse_turnover_model
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.models.warehouse_model import warehouse_model
from modules.Enums.transaction_type import enum_transaction_type


class creator(abstract_logic):

    def __init__(self):
        super().__init__()

    def dict_to_object(self, data) :
        # Проверка на список — если список, рекурсивно обрабатываем каждый элемент
        if isinstance(data, list):
            return [self.dict_to_object(item) for item in data]

        # Проверка на словарь
        if isinstance(data, dict):
            # Извлекаем имя класса из словаря
            class_name = data.pop('__class__', None)

            if class_name:
                # Получаем класс по имени
                klass = globals().get(class_name)

                if klass is None:
                    raise ValueError(f"Класс с именем {class_name} не найден.")

                # Обработка перечислений
                if issubclass(klass, Enum):
                    enum_value = data.get('__value__')

                    if enum_value is not None:
                        # Преобразуем строковое значение в элемент перечисления
                        if isinstance(enum_value, str):
                            # Преобразуем строку в верхний регистр, если это необходимо
                            enum_value = enum_value.capitalize()  # Преобразуем в формат, соответствующий классу Enum
                        if enum_value in klass.__members__:
                            return klass[enum_value]
                        else:
                            raise ValueError(f"'{enum_value}' is not a valid {klass.__name__}.")

                # Создаем объект класса, не вызывая __init__
                obj = klass.__new__(klass)

                # Рекурсивно назначаем атрибуты
                for key, value in data.items():
                    setattr(obj, key, self.dict_to_object(value))
                return obj
            else:
                # Обычный словарь, без указания класса
                return {key: self.dict_to_object(value) for key, value in data.items()}

        # Если это не словарь и не список, возвращаем значение как есть (например, строку или число)
        return data


    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)



