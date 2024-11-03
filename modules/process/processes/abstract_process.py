
from abc import ABC, abstractmethod

from modules.process.modified_list import modified_list


class abstract_process(ABC):

    @staticmethod
    @abstractmethod
    def start_process(data: modified_list):
        pass



