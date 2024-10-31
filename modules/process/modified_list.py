from datetime import datetime

from modules.exceptions.argument_exception import argument_exception

class modified_list(list):

    __file_path = None
    __block_period:datetime = None
    __date: datetime = None

    def __init__(self, iterable=None):
        if iterable is not None:
            super().__init__(iterable)
        else:
            super().__init__()

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value: str|None):
        argument_exception.isinstance(value, str|None)

        self.__file_path = value

    @property
    def block_period (self):
        return self.__block_period

    @block_period .setter
    def block_period (self, value: datetime):
        argument_exception.isinstance(value, datetime)

        self.__block_period = value.replace(hour=0, minute=0, second=0, microsecond=0)

    @property
    def date(self):
        return self.__block_period

    @date.setter
    def date(self, value: datetime):
        argument_exception.isinstance(value, datetime)

        self.__date = value.replace(hour=0, minute=0, second=0, microsecond=0)
