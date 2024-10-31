from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.reader.abstract_reader import abstract_reader
from modules.reader.format.json_reader import json_reader
from modules.reader.format_reading import format_reading


class reader(abstract_logic):
    __formats = {}

    def __init__(self, formats: dict=None) -> None:

        if formats is None:
            formats = {
                "JSON" : "json_reader"
            }
        else:
            argument_exception.isinstance(formats, dict)

        super().__init__()

        for key, class_name in formats.items():

            self.__formats[key] = globals()[class_name]


    def get_reader(self, _format: format_reading) -> None| abstract_reader:

        argument_exception.isinstance(_format, format_reading)

        if _format.name not in self.__formats.keys():
            self.set_exception(
                argument_exception(f"Указанный вариант формата {_format} не реализован!")

            )
            return None

        format_reader = self.__formats[_format.name]
        return format_reader()

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
