import json

from modules.data_reposity import data_reposity
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.reports.abstract_report import abstract_report
from modules.reports.format_reporting import format_reporting


class json_report(abstract_report):
    __indent = 3
    __ensure_ascii = False

    def __init__(self) -> None:
       super().__init__()
       self.extension = 'json'
       self.__format = format_reporting.JSON

    def create(self, data: list):
        argument_exception.isinstance_list(data, list, abstract_model)

        _json = data
        # _json = {}
        # _json[str(data[0].__class__.__name__)] = data


        self.result = json.dumps(
            _json,
            default=lambda o: o.get_dict(),
            indent=self.__indent,
            ensure_ascii=self.__ensure_ascii
        )


