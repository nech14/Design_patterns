from tokenize import group

from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.range_model import range_model


class nomenclature_model(abstract_model):

    __group: nomenclature_group_model = None
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


    def set_compare_mode(self, other_object: 'nomenclature_model') -> bool:
        if other_object is None: return False
        if not isinstance(other_object, nomenclature_model):
            raise argument_exception(argument_name="other_object")

        return super().set_compare_mode(other_object=other_object)


    @staticmethod
    def crate_nomenclature(
            nomenclatures_name: list[str],
            nomenclatures_group: list[nomenclature_group_model],
            nomenclatures_range: list[range_model]
    ):
        argument_exception.isinstance_list(nomenclatures_name, list, str)
        argument_exception.isinstance_list(nomenclatures_group, list, nomenclature_group_model)
        argument_exception.isinstance_list(nomenclatures_range, list, range_model)

        _list = []
        for i in range(len(nomenclatures_name)):
            n_m = nomenclature_model()
            n_m.name = nomenclatures_name[i]
            n_m.group = nomenclatures_group[i]
            n_m.range = nomenclatures_range[i]
            _list.append(n_m)
        return _list