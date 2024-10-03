from typing import Union

from modules.creator import creator
from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.models.ingredient_model import ingredient_model
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.receipt.receipt_model import receipt_model


class Creator_manager(abstract_logic):

    __object:abstract_model = None
    __object_dict:dict = None
    __creator: creator
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self, object_dict:dict):
        if object_dict is None:
            object_dict = {
                '__class__': 'range_model',
                'name': 'гр',
                'model_unique_code': '400b20fa-ae68-4a09-8e87-e50b83df0e35',
                'conversion_factor': 1,
                'base_unit_measurement': None
            }
        else:
            argument_exception.isinstance(object_dict, dict)

        self.__creator = creator()

        self.__object_dict = object_dict

    def get_object(self, data:dict=None):

        if data is None:
            data = self.__object_dict
        else:
            argument_exception.isinstance(data, dict)


        object_model = self.__creator.dict_to_object(data)

        self.__object = object_model

    @property
    def object(self) -> (Union)[
        receipt_model |
        range_model |
        nomenclature_model |
        nomenclature_group_model |
        ingredient_model |
        abstract_model
    ]:
        return self.__object



    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
