from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.reports.abstract_report import abstract_report
from modules.reports.format_reporting import format_reporting
from modules.reports.csv_report import csv_report


"""
Фабрика для формирования отчетов
"""
class report_factory(abstract_logic):
    __reports = {}

    def __init__(self) -> None:
        super().__init__()
        # Наборы отчетов
        self.__reports[ format_reporting.CSV ] = csv_report


    """
    Получить инстанс нужного отчета
    """
    def create(self, format: format_reporting) ->  abstract_report:
        argument_exception.isinstance(format, format_reporting)
        
        if format not in self.__reports.keys() :
            self.set_exception( argument_exception(f"Указанный вариант формата {format} не реализован!"))
            return None
        
        report = self.__reports[format]
        return report()
    

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
       



    
