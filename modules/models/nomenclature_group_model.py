from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model


class nomenclature_group_model(abstract_model):

    def set_compare_mode(self, other_object: 'nomenclature_group_model') -> bool:
        if not isinstance(other_object, nomenclature_group_model):
            raise argument_exception()
        return super().set_compare_mode(other_object)

