from tokenize import group

from modules.models.abstract_reference import abstract_reference
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.range_model import range_model


class nomenciature_model(abstract_reference):

    __group: nomenclature_group_model
    __range: range_model
    __max_name: int = 250



    @property
    def group(self):
        return self.__group


    @group.setter
    def group(self, value: nomenclature_group_model):
        if not isinstance(value, nomenclature_group_model):
            pass

        self.__group = value


    @property
    def range(self):
        return self.__range


    @range.setter
    def range(self, value: range_model):
        if not isinstance(value, range_model):
            pass

        self.__range = value



a = nomenciature_model()
a.name = "a"*600
print(len(a.name))