import json

from modules.exceptions.argument_exception import argument_exception
from modules.reader.abstract_reader import abstract_reader
from modules.reader.format_reading import format_reading
import os


class json_reader(abstract_reader):

    def __init__(self):
        super().__init__()
        self.extension = 'json'
        self.format = format_reading.JSON

    def read_file(self, file_path: str):
        argument_exception.isinstance(file_path, str)

        if not os.path.isfile(file_path):
            argument_exception("File does not exist at this path!", file_path)

        with open(file_path, 'r', encoding='utf-8') as jf:
            data = json.load(jf)

        return data