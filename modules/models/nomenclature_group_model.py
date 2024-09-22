from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model


class nomenclature_group_model(abstract_model):

    def set_compare_mode(self, other_object: 'nomenclature_group_model') -> bool:
        if not isinstance(other_object, nomenclature_group_model):
            raise argument_exception()
        return super().set_compare_mode(other_object)


    """
    Default группа - сырье (фабричный метод)
    """

    @staticmethod
    def default_group_source():
        item = nomenclature_group_model()
        item.name = "Сырье"
        return item


    """
       Default группа - замарозка (фабричный метод)
    """

    @staticmethod
    def default_group_cold():
        item = nomenclature_group_model()
        item.name = "Заморозка"
        return item