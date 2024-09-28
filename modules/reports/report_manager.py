import os.path
from copy import copy

from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception
from modules.reports.abstract_report import abstract_report
from modules.reports.format_reporting import format_reporting
from modules.reports.report_factory import report_factory
from modules.settings.settings_manager import Settings_manager


class Report_manager(abstract_logic):

    __factory:report_factory
    __format = format_reporting.JSON
    __report: abstract_report = None
    __report_settings = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Report_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self, report_settings:dict=None) -> None:
        if report_settings is None:
            self.__report_settings = Settings_manager().report_settings

        else:
            argument_exception.isinstance(report_settings, dict)
            self.__report_settings = report_settings


        self.__update_factory()


    @property
    def report_settings(self):
        return self.__report_settings

    @report_settings.setter
    def report_settings(self, value: dict):
        argument_exception.isinstance(value, dict)
        self.__report_settings = value
        self.__update_factory()


    def __update_factory(self):
        self.__factory = report_factory(self.__report_settings)



    def create(self, data:list[dict], _format=None):
        if _format is None:
            _format = self.format
        argument_exception.isinstance(_format, format_reporting)

        create_cl = self.__factory.create(_format)
        create_cl.create(data = data)
        self.__report = create_cl

    def save(self, _path: str):
        argument_exception.isinstance(_path, str)

        if self.__report == "" or self.__report is None:
            length_exception.length_zero()


        if os.path.exists(_path) and os.path.isdir(_path):
            argument_exception("Wrong way!")

        try:
            # Запись в файл
            with open(f"{_path}/report.{self.__report.extension}", "w", encoding="utf-8") as f:
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

