from pathlib import Path

from modules.exceptions.argument_exception import argument_exception


class modified_list(list):

    __file_path = None

    def __init__(self, iterable=None):
        if iterable is not None:
            super().__init__(iterable)
        else:
            super().__init__()

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value: str):
        argument_exception.isinstance(value, str)

        self.__file_path = value


