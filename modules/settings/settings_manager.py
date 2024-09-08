
from modules.settings.settings_base import Settings
import os
import json

"""
Менеджер настроек
"""


class Settings_manager:
    __file_name = "settings.json"
    __settings: Settings = None
    __text_encoding: str = 'windows-1251'


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings_manager, cls).__new__(cls)
        return cls.instance


    def __init__(self) -> None:
        if self.__settings is None:
            self.__settings = self.__default_setting()


    def read_settings(self, file_name: str, text_encoding: str=None):
        if not text_encoding is None and isinstance(text_encoding, str):
            self.__text_encoding = text_encoding

        if isinstance(file_name, str) and file_name != "":
           self.__file_name = file_name


    def go_to_norm_encod(self, s:str):
        if not isinstance(s, str):
            return s
        return s.encode(self.__text_encoding).decode('utf-8')


    """
    Открыть и загрузить настройки
    """
    def open(self, file_name: str = "", file_path: str = ""):
        if not isinstance(file_name, str) and not isinstance(file_path, str):
            raise TypeError("Некорректно переданы параметры!")

        if file_name != "":
            self.__file_name = file_name

        try:
            if file_path != "":
                full_name = f"{file_path}{os.sep}{self.__file_name}"
            else:
                full_name = f".{os.sep}{os.curdir}{os.sep}data{os.sep}{self.__file_name}"

            stream = open(full_name)
            data = json.load(stream)

            # Список полей от типа назначения
            fields = list(filter(lambda x: not x.startswith("_"), dir(self.__settings.__class__)))

            # Заполняем свойства
            for field in fields:
                keys = list(filter(lambda x: x == field, data.keys()))
                if len(keys) != 0:
                    value = self.go_to_norm_encod(data[field])
                    # Если обычное свойство - заполняем.
                    if not isinstance(value, list) and not isinstance(value, dict) and value != "":
                        setattr(self.__settings, field, value)

            return True
        except:
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
