
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.reports.abstract_report import abstract_report
from modules.reports.format_reporting import format_reporting


class markdown_report(abstract_report):

    __separator = "|"

    def __init__(self) -> None:
       super().__init__()
       self.extension = "md"
       self.__format = format_reporting.MARKDOWN


    def create(self, data: list[abstract_model]):
        argument_exception.isinstance(data, list)

        self.result = ""

        fields = data[0].get_dict().keys()

        self.result += self.__separator
        for field in fields:
            self.result += f"{field}{self.__separator}"

        self.result += '\n'
        for field in fields:
            self.result += self.__separator + '-' * len(field)
        self.result += self.__separator+'\n'

        for row in data:
            _dict = row.get_dict()
            self.result += self.__separator

            for key in _dict.keys():
                value = _dict[key]
                if isinstance(value, list):
                    _str = "["
                    for i in value:
                        if isinstance(i, dict):
                            _str += "("
                            for j in i.keys():
                                if isinstance(i[j], dict):
                                    _str += f"{i[j]["name"]},"
                                else:
                                    _str += f"{i[j]},"
                            _str = _str[:-1] + "),"
                        else:
                            _str += f"{i},"
                    _str = _str[:-1] + "]"
                    self.result += f"{_str}{self.__separator}"

                elif isinstance(value, dict):
                    _str = "["
                    for i in value.keys():
                        _str += f"{value[i]},"
                    _str = _str[:-1] + "]"
                    self.result += f"{_str}{self.__separator}"

                else:
                    self.result += f"{value}{self.__separator}"

            self.result += '\n'





