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
    __objects: list[abstract_model] = []

    @property
    def objects(self):
        return self.__objects

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self, object_dict:dict|list=None):
        if object_dict is None:
            object_dict = {
                '__class__': 'range_model',
                'name': 'гр',
                'model_unique_code': '400b20fa-ae68-4a09-8e87-e50b83df0e35',
                'conversion_factor': 1,
                'base_unit_measurement': None
            }
        else:
            argument_exception.isinstance(object_dict, dict|list)

        self.__creator = creator()

        self.__object_dict = object_dict


    def get_object(self, data:dict=None):

        if data is None:
            data = self.__object_dict
        else:
            argument_exception.isinstance(data, dict)

        object_model = self.__creator.dict_to_object(data)
        self.__object = self.add_new_item(object_model)




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



    def add_new_item(self, item: abstract_model|list[abstract_model]|dict):
        argument_exception.isinstance(item, abstract_model|list|dict)

        if len(self.__objects) == 0:
            self.__objects.append(item)
            return self.__objects[-1]

        if isinstance(item, dict):
            return self.add_item_dict(item)

        elif isinstance(item, abstract_model):
            return self.item_add(item)

        elif isinstance(item, list):
            return self.add_item_list(item)


        self.__objects.append(item)
        return  self.__objects[-1]


    def item_add(self, item):
        for i in range(len(self.__objects)):
            if self.__objects[i].unique_code == item.unique_code:
                for attr, value in vars(item).items():
                    setattr(self.__objects[i], attr, value)
                return self.__objects[i]
        else:
            self.__objects.append(item)
            return item


    def add_item_list(self, item_list: list[abstract_model]):

        obj_list = []

        for o in item_list:

            obj_list.append(self.add_new_item(o))

            # for i in range(len(self.__objects)):
            #     if self.__objects[i].unique_code == o.unique_code:
            #         obj_list.append(self.__objects[i])
            #         break
            # else:
            #     self.__objects.append(o)
            #     obj_list.append(self.__objects[-1])

        return obj_list


    def add_item_dict(self, item_dict):

        obj_dict = {}

        for k, v in item_dict.items():
            obj_dict[k] = self.add_new_item(v)

        return obj_dict


    def remove_item(self, item):
        self.__objects.remove(item)


    def update_original_item(self, path_item: abstract_model):
        argument_exception.isinstance(path_item, abstract_model)

        for i in range(len(self.__objects)):
            if path_item is self.__objects[i]:
                return self.__objects[i]
        else:
            self.__objects.append(path_item)
            return self.__objects[-1]
