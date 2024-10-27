
from abc import ABC, abstractmethod


class abstract_process(ABC):

    @staticmethod
    @abstractmethod
    def start_process(data: list):
        pass



