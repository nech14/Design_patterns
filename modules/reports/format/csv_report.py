
from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception
from modules.models.abstract_model import abstract_model
from modules.reports.format_reporting import format_reporting
from modules.reports.abstract_report import abstract_report

"""
Ответ формирует набор данных в формате CSV
"""
class csv_report(abstract_report):

    __separator = ";"


    def __init__(self) -> None:
       super().__init__()
       self.extension = "csv"
       self.__format = format_reporting.CSV

 
    def create_last(self, data: list[abstract_model]):
        argument_exception.isinstance_list(data, list, abstract_model)
        if len(data) == 0:
            raise length_exception.length_zero()
        

        first_model = data[0]

        # Список полей от типа назначения    
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(first_model.__class__, x )),  dir(first_model) ))


        # Заголовок
        for field in fields:
            self.result += f"{str(field)}{self.__separator}"

        self.result += "\n"    

        # Данные
        for row in data:
            if row.is_method_defined_in_child('__str__'):
                self.result += f"{str(row)}{self.__separator}"
            else:
                for field in fields:
                    value = getattr(row, field)
                    if isinstance(value, list) and all(isinstance(item, abstract_model) for item in value):
                        self.result += f"["
                        for item in value:
                            self.result += f"{item.name},"
                        self.result = self.result[:-1] + f"]"
                    elif isinstance(value, abstract_model):
                        self.result += f"{str(value.name)}{self.__separator}"
                    else:
                        self.result += f"{str(value)}{self.__separator}"

            self.result += "\n"


    def create(self, data: list[abstract_model]):
        argument_exception.isinstance(data, list)

        self.result = ""

        fields = data[0].get_dict().keys()

        for field in fields:
            self.result += f"{field}{self.__separator}"

        self.result += '\n'

        for row in data:
            _dict = row.get_dict()

            for key in _dict.keys():
                value = _dict[key]

                if isinstance(value, list):
                    _str = "["
                    for i in value:
                        if isinstance(i, dict):
                            _str += "("
                            for j in i.keys():
                                if isinstance(i[j], dict):
                                    _str += f'{i[j]["name"]},'
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










