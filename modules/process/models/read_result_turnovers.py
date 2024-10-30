import json
import os
from pathlib import Path

from modules.creator_manager import Creator_manager
from modules.exceptions.argument_exception import argument_exception
from modules.process.models.abstract_process import abstract_process
from modules.process.modified_list import modified_list


class read_result_turnovers(abstract_process):

    @staticmethod
    def start_process(data: modified_list = None):
        if data is None:
            data = modified_list()

        file_path = data.file_path

        if file_path is None or file_path == "":
            root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
            file_path = os.path.join(root_path, "result", "result_process.json")
        else:
            argument_exception.isinstance(file_path, str)

        file_path = Path(file_path)

        # Проверка существования файла
        if file_path.is_file():
            with file_path.open("r") as file:
                data = json.load(file)  # Чтение JSON и преобразование в dict
        else:
            raise argument_exception(message=f"Файл {file_path} не существует.")

        creator_manager = Creator_manager(data)
        creator_manager.get_object()

        return creator_manager.object
