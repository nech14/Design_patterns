
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.range_model import range_model


class nomenciature_model(abstract_model):

    __group: nomenclature_group_model
    __range: range_model
    __max_name: int = 250



    @property
    def group(self):
        return self.__group


    @group.setter
    def group(self, value: nomenclature_group_model):
        if not isinstance(value, nomenclature_group_model):
            raise argument_exception()

        self.__group = value


    @property
    def range(self):
        return self.__range


    @range.setter
    def range(self, value: range_model):
        if not isinstance(value, range_model):
            raise argument_exception()

        self.__range = value


    def set_compare_mode(self, other_object: 'nomenciature_model') -> bool:
        if other_object is None: return False
        if not isinstance(other_object, nomenciature_model):
            raise argument_exception()

        return super().set_compare_mode(other_object=other_object)