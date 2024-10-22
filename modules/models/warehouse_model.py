from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model

class warehouse_model(abstract_model):

    __address: str = ""



    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        argument_exception.isinstance(value, str)

        self.__address = value

    @staticmethod
    def get_base_warehouse(
            name="test_warehouse",
            address="test_address"
    ):
        item_warehouse = warehouse_model()
        item_warehouse.name = name
        item_warehouse.address = address
        return item_warehouse