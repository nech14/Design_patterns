from abc import ABC, abstractmethod

from modules.exceptions.argument_exception import argument_exception
from modules.reader.format_reading import format_reading


class abstract_reader(ABC):
    __format: format_reading.JSON
    __result: dict
    __extension: str

    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, value: format_reading):
        argument_exception.isinstance(value, format_reading)

        self.__format = value


    @property
    def result(self):
        return self.__result

    @abstractmethod
    def read_file(self, file_path: str):
        pass


    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        self.__extension = value