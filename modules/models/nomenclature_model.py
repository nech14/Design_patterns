from tokenize import group

from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.range_model import range_model


class nomenclature_model(abstract_model):

    __group: nomenclature_group_model = None
    __range: range_model
    __max_name: int = 250

    __base_nomenclatures_name = ["Пшеничная мука", "Сахар", "Сливочное масло", "Яйца", "Ванилин(щепотка)"]
    __base_nomenclatures_groupe = [nomenclature_group_model.default_group_source() for i in range(5)]
    __base_nomenclatures_range = [range_model.default_range_grams(), range_model.default_range_grams(),
                                  range_model.default_range_grams(), range_model.default_range_pieces(),
                                  range_model.default_range_grams()]

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
        if not isinstance(other_object, nomenclature_model|str):
            raise argument_exception(argument_name="other_object")

        return super().set_compare_mode(other_object=other_object)


    @staticmethod
    def crate_nomenclatures(
            nomenclatures_name: list[str],
            nomenclatures_group: list[nomenclature_group_model],
            nomenclatures_range: list[range_model]
    ) -> list['nomenclature_model']:
        argument_exception.isinstance_list(nomenclatures_name, list, str)
        argument_exception.isinstance_list(nomenclatures_group, list, nomenclature_group_model)
        argument_exception.isinstance_list(nomenclatures_range, list, range_model)

        _list = []
        for i in range(len(nomenclatures_name)):
            _list.append(
                nomenclature_model.create_nomenclature(
                    name = nomenclatures_name[i],
                    group = nomenclatures_group[i],
                    range = nomenclatures_range[i]
                )
            )
        return _list

    @staticmethod
    def default_nomenclature():
        return nomenclature_model.crate_nomenclatures(
            nomenclature_model.__base_nomenclatures_name,
            nomenclature_model.__base_nomenclatures_groupe,
            nomenclature_model.__base_nomenclatures_range,
        )

    @staticmethod
    def create_nomenclature(name: str, group: nomenclature_group_model, range: range_model):
        argument_exception.isinstance(name, str)
        argument_exception.isinstance(group, nomenclature_group_model)
        argument_exception.isinstance(range, range_model)
        n_m = nomenclature_model()
        n_m.name = name
        n_m.group = group
        n_m.range = range
        return n_m


    @staticmethod
    def check_name(nomenclature: 'nomenclature_model', name:str) -> bool:
        argument_exception.isinstance(nomenclature, nomenclature_model)
        argument_exception.isinstance(name, str)

        return nomenclature.name == name

    @staticmethod
    def found_by_name(nomenclatures: list['nomenclature_model'], name:str):
        argument_exception.isinstance_list(nomenclatures, list, nomenclature_model)
        argument_exception.isinstance(name, str)

        for nomenclature in nomenclatures:
            if nomenclature.name == name:
                return nomenclature

        return None