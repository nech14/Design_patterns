from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception
from modules.reports.format_reporting import format_reporting
from modules.reports.abstract_report import abstract_report


"""
Ответ формирует набор данных в формате CSV
"""
class csv_report(abstract_report):

    def __init__(self) -> None:
       super().__init__()
       self.__format = format_reporting.CSV

 
    def create(self, data: list):
        argument_exception.isinstance(data, list)
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
            for field in fields:
            
                value = getattr(row, field)
                self.result += f"{str(value)};"
            self.result += "\n"











        
        