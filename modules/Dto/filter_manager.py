import inspect
from typing import get_type_hints

from modules.Dto.base_filter import base_filter
from modules.Dto.filter_objects import filter_objects
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.models.range_model import range_model



class Filter_manager():
    __filter_object = filter_objects.base_filter
    __filter_property: list[str] = None
    __filter: base_filter = None
    __property_one_for_heirs = False
    inner_properties = None


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Filter_manager, cls).__new__(cls)
        return cls.instance


    def __init__(self):
        pass


    @property
    def filter(self):
        return self.__filter


    @property
    def filter_property(self):
        return self.__filter_property


    @property
    def filter_object(self):
        return self.__filter_object


    @filter_object.setter
    def filter_object(self, value: filter_objects):
        argument_exception.isinstance(value, filter_objects)

        self.__filter_object = value


    def update_filter_property(self):
        attributes  = inspect.getmembers(self.__filter_object.value)

        property_methods  = []

        for name, attribute in attributes:
            if isinstance(attribute, property):
                property_methods.append(name)

        self.__filter_property = property_methods

    # def update_filter_properts(self):
    #     self.__filter_property = self.__get_attributes(self.__filter_object.value)
    #
    # def __get_attributes(self, obj, parent_name=''):
    #     attributes = inspect.getmembers(obj)
    #     property_methods = []
    #
    #     for name, attribute in attributes:
    #         # Проверяем, если атрибут является свойством
    #         if isinstance(attribute, property):
    #             full_name = f"{parent_name}.{name}" if parent_name else name
    #
    #             # Получаем аннотации типа для свойства
    #             type_hints = get_type_hints(obj, globalns=globals())
    #             property_type = type_hints.get(name, None)
    #
    #             # Добавляем имя свойства и тип
    #             property_methods.append(full_name)
    #
    #             # Если аннотация типа указана как строка, мы её выводим
    #             if property_type is None:
    #                 property_type = attribute.fget.__annotations__.get('return', None)
    #                 property_methods.append(f"Type: {property_type}")
    #             else:
    #                 property_methods.append(f"Type: {property_type}")
    #
    #             # Получаем значение свойства, вызывая его
    #             prop_value = getattr(obj, name)
    #
    #             # Проверяем, является ли значение экземпляром класса и не None
    #             if not property_type is None:
    #                 print("gggg")
    #                 property_methods.extend(
    #                     self.__get_attributes(prop_value, full_name)
    #                 )  # Рекурсивно ищем свойства в объекте
    #
    #     return property_methods


    def update_filter(self):
        # Функция, создающая геттер для свойства
        def make_getter(attr_name):
            return lambda self: getattr(self, f"_{attr_name}")

        # Функция, создающая сеттер для свойства
        def make_setter(attr_name):
            return lambda self, value: setattr(self, f"_{attr_name}", value)

        # Функция для динамического создания конструктора __init__
        def init(self, filter_property):
            # Устанавливаем изначальные значения в ""
            for attr in filter_property:
                setattr(self, f"_{attr}", "")  # Установка пустой строки как начального значения

        # Словарь для хранения атрибутов и свойств
        class_dict = {'__init__': init}  # Добавляем __init__ в словарь класса

        # Добавляем приватные атрибуты и свойства для каждого элемента из списка attributes
        for attr in self.__filter_property:
            class_dict[f"_{attr}"] = ""  # Приватное поле
            class_dict[attr] = property(make_getter(attr), make_setter(attr))  # Свойство

        # Создаем класс с использованием type()
        new_filter = type(f"{self.__filter_object.name}", (base_filter,), class_dict)

        self.__filter = new_filter(self.__filter_property)


    def update_property_filter(self, **kwargs):
        for key, value in kwargs.items():
            if not key in self.__filter_property:
                raise argument_exception(argument_name=key)

            setattr(self.__filter, key, value)