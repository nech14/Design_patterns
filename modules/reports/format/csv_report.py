from rasterio.rio.shapes import feature_gen

from modules.data_reposity import data_reposity
from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception
from modules.models.abstract_model import abstract_model
from modules.models.range_model import range_model
from modules.reports.format_reporting import format_reporting
from modules.reports.abstract_report import abstract_report
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service

"""
Ответ формирует набор данных в формате CSV
"""
class csv_report(abstract_report):

    def __init__(self) -> None:
       super().__init__()
       self.__format = format_reporting.CSV

 
    def create(self, data: list[abstract_model]):
        argument_exception.isinstance_list(data, list, abstract_model)
        if len(data) == 0:
            raise length_exception.length_zero()
        

        first_model = data[0]

        # Список полей от типа назначения    
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(first_model.__class__, x )),  dir(first_model) ))


        # Заголовок
        for field in fields:
            self.result += f"{str(field)};"

        self.result += "\n"    

        # Данные
        for row in data:
            if row.is_method_defined_in_child('__str__'):
                self.result += f"{str(row)};"
            else:
                for field in fields:
                    value = getattr(row, field)
                    if isinstance(value, list) and all(isinstance(item, abstract_model) for item in value):
                        self.result += f"["
                        for item in value:
                            self.result += f"{item.name},"
                        self.result = self.result[:-1] + f"]"
                    elif isinstance(value, abstract_model):
                        self.result += f"{str(value.name)};"
                    else:
                        self.result += f"{str(value)};"

            self.result += "\n"


