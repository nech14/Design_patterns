
from abc import ABC, abstractmethod

from modules.models.abstract_model import abstract_model


class abstract_observer(ABC):

    @abstractmethod
    def update(self, item: abstract_model):
        pass


