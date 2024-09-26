from modules.data_reposity import data_reposity
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.reports.abstract_report import abstract_report
from modules.reports.format_reporting import format_reporting
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service


class rtf_report(abstract_report):

    def __init__(self) -> None:
       super().__init__()
       self.extension = "rtf"
       self.format = format_reporting.RTF

    def __dict_to_rtf(self, data):
        rtf_string = r"{\rtf1\ansi\ansicpg1252\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Arial;}}"
        rtf_string += r"{\*\generator Riched20 10.0.18362;}"

        # Добавляем каждый элемент списка в RTF
        for item in data:
            rtf_string += r"{\pard\fs24 "  # Начинаем новый параграф, задаем размер шрифта

            # Проверяем, является ли элемент объектом класса
            if hasattr(item, 'get_dict'):
                item_dict = item.get_dict()
                for key, value in item_dict.items():
                    rtf_string += fr"{key}: {value}\line "  # Добавляем ключ и значение, затем перенос строки
            elif isinstance(item, dict):
                for key, value in item.items():
                    rtf_string += fr"{key}: {value}\line "  # Если элемент словарь
            else:
                rtf_string += fr"Item: {item}\line "  # Если элемент не словарь и не объект

            rtf_string += r"}\par "  # Закрываем параграф и переходим к следующему

        rtf_string += r"}"  # Закрываем RTF документ
        return rtf_string


    def create(self, data: list):

        argument_exception.isinstance_list(data, list, abstract_model)

        self.result = self.__dict_to_rtf(data)

