import os.path

from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception
from modules.reports.abstract_report import abstract_report
from modules.reports.format_reporting import format_reporting
from modules.reports.report_factory import report_factory


class Report_manager(abstract_logic):

    __factory = report_factory()
    __format = format_reporting.CSV
    __report: abstract_report = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Report_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self, _format_reporting= format_reporting.CSV) -> None:
        self.__factory = report_factory()
        self.__format = _format_reporting



    def create(self, data:list[dict], format=None):
        if format is None:
            format = self.format
        argument_exception.isinstance(format, format_reporting)

        create_cl = self.__factory.create(format)
        create_cl.create(data = data)
        self.__report = create_cl

    def save(self, path: str):
        argument_exception.isinstance(path, str)

        if self.__report == "" or self.__report is None:
            length_exception.length_zero()


        if os.path.exists(path=path) and os.path.isdir(path=path):
            argument_exception("Wrong way!")

        try:
            # Запись в файл
            with open(f"{path}/report.{self.__report.extension}", "w", encoding="utf-8") as f:
                f.write(self.__report.result)
        except Exception as e:
            argument_exception("Problems with saving!", f"{e}")



    @property
    def report(self):
        return self.__report

    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, value: format_reporting):
        argument_exception.isinstance(value, format_reporting)

        self.__format = value


    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

