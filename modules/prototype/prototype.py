import inspect

from modules.Dto.base_filter import base_filter
from modules.Dto.filtration_type import filtration_type
from modules.exceptions.argument_exception import argument_exception
from modules.prototype.abstract_prototype import abstract_prototype

"""
Реализация простого прототипа на примере номенклатуры
"""
class prototype(abstract_prototype):

    __list_fields: list[str] = None
    __property_one_for_heirs = False

    @staticmethod
    def filter_EQUALS(value1, value2):
        return value1 == value2

    @staticmethod
    def filter_LIKE(value1, value2):
        return value2 in value1

    @staticmethod
    def filter_INTERVAL(value1, value2):
        return value2[0].date() <= value1.date() <= value2[1].date()

    __filtration_types = [filter_EQUALS, filter_LIKE, filter_INTERVAL]


    def __init__(self, source: list=[], list_fields:list[str]=[]) -> None:
        super().__init__(source)
        self.__list_fields = list_fields

    def create(
            self, data: list,
            filterDto: base_filter,
            list_fields:list[str]=[],
            filter_type:filtration_type = filtration_type.LIKE
    ):
        argument_exception.isinstance(filterDto, base_filter)
        argument_exception.isinstance_list(list_fields, list, str)
        argument_exception.isinstance(filter_type, filtration_type)
        super().create(data, filterDto)
        self.data = data
        self.__list_fields = list_fields
        for f in range(len(self.__list_fields)):
            self.data = self.filter_by_field(self.data, f, filterDto, filter_type=filter_type)
        instance = prototype(self.data, self.__list_fields)
        return instance


    @property
    def list_fields(self):
        return self.__list_fields

    @list_fields.setter
    def list_fields(self, value: list[str]):
        argument_exception.isinstance_list(value, list, str)

        self.__list_fields = value

    def filter_by_field(
            self,
            source:list,
            index_field: int,
            filter: base_filter,
            filter_type:filtration_type = filtration_type.EQUALS,
            property_one_for_heirs = False
    ):
        argument_exception.isinstance(source, list)
        argument_exception.isinstance(index_field, int)
        argument_exception.isinstance(filter, base_filter)
        argument_exception.isinstance(filter_type, filtration_type)
        argument_exception.isinstance(property_one_for_heirs, bool)


        if index_field >= len(self.__list_fields) or self.__list_fields[index_field] == "":
            return source

        result = []
        name_field = self.__list_fields[index_field]

        if getattr(filter, name_field) == "":
            return source

        name_field_filter = name_field
        name_field = name_field.split('.')

        for item in source:
            if len(name_field) > 1:
                attr1 = item
                for attr in name_field:
                    if isinstance(attr1, list):
                        attr1 = self.__list_attr(attr1, attr)
                    else:
                        attr1 = getattr(attr1, attr)
            else:
                attr1 = getattr(item, name_field[0])

            if self.__filtration_types[filter_type.value-1](
                    attr1,
                    getattr(filter, name_field_filter)
            ):
                result.append(item)
            elif property_one_for_heirs:
                item_fields = self.__get_property_methods(item)
                matching_indices = [i for i, item in enumerate(item_fields) if item.rsplit('.', 1)[-1] == name_field]

                for index in matching_indices:
                    if self.__filtration_types[filter_type.value-1](
                            self.__get_nested_attribute(item, item_fields[index]),
                            getattr(filter, name_field_filter)
                    ):
                        result.append(item)
                        break


        return result

    def __list_attr(self, attr1, attr):
        result_list = []

        for a in attr1:
            if isinstance(a, list):
                a_item = self.__list_attr(a, attr)
            else:
                a_item = getattr(a, attr)

            result_list.append(a_item)
        return result_list



    def __get_property_methods(self, obj, path:str=""):
        argument_exception.isinstance(path, str)
        results = []

        for name, value in inspect.getmembers(obj.__class__):
            if isinstance(value, property):
                full_path = f"{path}.{name}" if path else name

                prop_value = getattr(obj, name)

                if not isinstance(prop_value, (str, int, float, bool, tuple, list, dict)):
                    results.extend(self.__get_property_methods(prop_value, full_path))
                else:
                    results.append(full_path)

        return results


    def __get_nested_attribute(self, obj, attr_path:str):
        argument_exception.isinstance(attr_path, str)
        attrs = attr_path.split('.')

        for attr in attrs:
            obj = getattr(obj, attr, None)
            if obj is None:
                raise argument_exception(argument_name=attr)

        return obj

