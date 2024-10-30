import json
import os
from pathlib import Path

from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.process.models.abstract_process import abstract_process
from modules.process.modified_list import modified_list


class save_result_turnovers(abstract_process):

    @staticmethod
    def start_process(data: modified_list):

        argument_exception.isinstance_list(data, modified_list, abstract_model)

        dict_list = []
        for item in data:
            item:abstract_model
            dict_list.append(item.get_dict())

        file_path = data.file_path
        if file_path is None or file_path == "":
            root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
            file_path = os.path.join(root_path, "result", "result_process.json")
        else:
            argument_exception.isinstance(file_path, str)

        file_path = Path(file_path)

        try:
            # Создание папки, если её нет
            file_path.parent.mkdir(parents=True, exist_ok=True)

            with file_path.open("w") as file:
                json.dump(dict_list, file, indent=4)

            return True

        except Exception as e:
            return False