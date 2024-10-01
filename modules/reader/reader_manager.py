import os

from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.reader.format_reading import format_reading
from modules.reader.reader import reader
from modules.settings.settings_manager import Settings_manager


class Reader_manager(abstract_logic):

    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    __file_path = ""
    __reader: reader
    __reader_settings: dict
    __result: dict = None
    __format_reader: format_reading = format_reading.JSON


    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Reader_manager, cls).__new__(cls)
        return cls.instance


    def __init__(
            self,
            file_path: str=None,
            reader_settings: dict = None,
            format_reader: format_reading = format_reading.JSON
    ) -> None:
        if file_path is None:
            file_path = self.file_path + '/reports/range/report.json'
        else:
            argument_exception.isinstance(file_path, str)
            self.__file_path = file_path

        if reader_settings is None:
            self.__reader_settings = Settings_manager.default_reader_settings()
        else:
            argument_exception.isinstance(reader_settings, dict)
            self.__reader_settings = reader_settings

        argument_exception.isinstance(format_reader, str)
        self.__format_reader = format_reader
        self.__update_reader()


    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value: str):
        argument_exception.isinstance(value, str)
        self.__file_path = value


    @property
    def reader_settings(self):
        return self.__reader_settings


    @reader_settings.setter
    def reader_settings(self, value:dict):
        argument_exception.isinstance(value, dict)
        self.__reader_settings = value
        self.__update_reader()


    def __update_reader(self):
        self.__reader = reader(formats=self.__reader_settings)

    @property
    def format_reader(self):
        return self.__format_reader

    @format_reader.setter
    def format_reader(self, value: format_reading):
        argument_exception.isinstance(value, format_reading)
        self.__format_reader = value

    @property
    def result(self):
        return self.__result

    def open(self, file_path: str=None):
        if file_path is None:
            file_path = self.file_path
        else:
            argument_exception.isinstance(file_path, str)

        try:

            if not os.path.isfile(file_path):
                argument_exception("File does not exist at this path!", file_path)

            _reader = self.__reader.get_reader(self.__format_reader)

            if not _reader is None:
                self.__result = _reader(self.__file_path)
            else:
                self.__result = None

            return True
        except Exception as ex:
            self.set_exception(ex)
            return False

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)