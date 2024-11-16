from datetime import datetime
from enum import Enum

from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.abstract_logic import abstract_logic
from modules.reports.format_reporting import format_reporting
from modules.settings.settings_base import Settings
import os
import json

"""
Менеджер настроек
"""


class Settings_manager(abstract_logic):
    __file_name = "settings.json"
    __file_path = f"data/{__file_name}"
    __settings: Settings = None
    __text_encoding: str = 'utf-8'
    __report_settings = {}
    __report_enum: Enum = format_reporting.JSON
    __reader_settings: dict = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        if self.__settings is None:
            self.__settings = self.__default_setting()
            self.__default_report_settings()


    def save_block_period(self, file_path: str = ""):
        argument_exception.isinstance(file_path, str)
        if file_path == "":
            file_path = self.__file_path

        with open(file_path, 'r', encoding=self.__text_encoding) as f:
            data = json.load(f)
            data["block_period"] = self.settings.block_period.strftime("%Y-%m-%d")


        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)


    """
    Открыть и загрузить настройки
    """

    def open(self, file_name: str = "", file_path: str = "", text_encoding: str = ""):
        if not isinstance(file_name, str) or not isinstance(file_path, str):
            raise argument_exception()

        if not isinstance(text_encoding, str):
            raise argument_exception()

        if file_name != "":
            self.__file_name = file_name


        if text_encoding != "":
            self.__text_encoding = text_encoding

        try:
            if file_path != "":
                self.file_path =f"{file_path}{os.sep}{self.__file_name}"
                full_name = self.file_path
            else:
                self.file_path = f"..{os.sep}..{os.sep}data{os.sep}{self.__file_name}"
                full_name = self.file_path



            with open(full_name, encoding=self.__text_encoding) as stream:
                data = json.load(stream)

                # Список полей от типа назначения
                fields = list(filter(lambda x: not x.startswith("_"), dir(self.__settings.__class__)))

                # Заполняем свойства
                for field in fields:
                    keys = list(filter(lambda x: x == field, data.keys()))
                    if len(keys) != 0:
                        value = data[field]
                        # Если обычное свойство - заполняем.
                        if not isinstance(value, list) and not isinstance(value, dict) and value != "":
                            setattr(self.__settings, field, value)


            return True
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            self.__settings = self.__default_setting()
            return False

    """
    Загруженные настройки
    """

    @property
    def settings(self):
        return self.__settings

    """
    Набор настроек по умолчанию
    """

    def __default_setting(self):
        data = Settings()
        data.inn = "380080920202"
        data.organization_name = "Рога и копыта (default)"
        data.BIC = "123456789"
        data.type_of_property = "12345"
        data.score = "12345678910"

        return data


    @staticmethod
    def default_reader_settings():
        return {"JSON" : "json_reader"}


    @property
    def reader_settings(self):
        return self.__reader_settings

    @reader_settings.setter
    def reader_settings(self, value: dict):
        argument_exception.isinstance(value, dict)
        self.__reader_settings = value



    def open_report_settings(self, _path: str):
        argument_exception.isinstance(_path, str)
        if not os.path.isfile(_path):
            argument_exception("File does not exist", _path)

        with open(_path, 'r', encoding=self.__text_encoding) as file:
            data = json.load(file)

        self.__report_settings = data
        # self.__report_enum = Enum("report_format",  self.__report_settings.keys())


    def __default_report_settings(self):
        self.__report_settings = {}
        self.__report_settings["JSON"] = "json_report"


    @property
    def report_settings(self):
        return self.__report_settings

    @property
    def report_enum(self):
        return self.__report_enum


    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)


