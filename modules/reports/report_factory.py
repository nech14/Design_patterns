import os

from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.reports.abstract_report import abstract_report
from modules.reports.format_reporting import format_reporting
import importlib
from pathlib import Path

# Словарь для хранения импортированных классов
imported_classes = {}


"""
Фабрика для формирования отчетов
"""
class report_factory(abstract_logic):
    __reports = {}
    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    __path_format_dir = Path(__root_dir+r'\format')

    __base_format = None

    __last_three_parts = str(Path(*list(__path_format_dir.parts)[-3:]))

    def __init__(self) -> None:
        super().__init__()
        files = os.listdir(self.__path_format_dir)
        # Фильтруем только файлы (исключая папки)
        files = [f for f in files if f not in ['__init__.py', '__pycache__']]

        # Фильтруем только файлы и извлекаем название до символа "_"
        names_before_underscore = [f.split('_')[0].upper() for f in files]

        for _enum in format_reporting:
            if _enum.name in names_before_underscore:

                class_name = str(files[names_before_underscore.index(_enum.name)][:-3])
                class_path = f"{self.__last_three_parts.replace('/', '.').replace('\\', '.')}.{class_name}"

                # Импортируем модуль и получаем класс
                module = importlib.import_module(class_path)

                # Получаем класс из модуля
                cls = getattr(module, class_name)

                # Сохраняем класс в словаре
                imported_classes[class_name] = cls

                self.__reports[_enum] = getattr(module, class_name)

        __base_format = self.__reports[list(self.__reports.keys())[0]]




    """
    Получить инстанс нужного отчета
    """
    def create(self, format: format_reporting) ->  abstract_report | None:
        argument_exception.isinstance(format, format_reporting)
        
        if format not in self.__reports.keys() :
            self.set_exception( argument_exception(f"Указанный вариант формата {format} не реализован!"))
            return None
        
        report = self.__reports[format]
        return report()


    def create_default(self):

        return self.__base_format()




    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
       



    
