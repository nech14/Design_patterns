
from abc import ABC, abstractmethod

from modules.models.abstract_model import abstract_model


class abstract_service(ABC):

    __data_reposity = None

    @property
    def data_reposity(self):
        return self.__data_reposity


    @abstractmethod
    def get_item(self, ID: str):
        pass


    @abstractmethod
    def put_item(self, item: abstract_model):
        pass


    @abstractmethod
    def path_item(self, item: abstract_model):
        pass


    @abstractmethod
    def delete_item(self, ID: str):
        pass


