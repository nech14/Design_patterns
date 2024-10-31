import json
import os
import unittest
from pathlib import Path

from modules.models.abstract_model import abstract_model
from modules.models.warehouse_turnover_model import warehouse_turnover_model
from modules.process.processes.save_result_turnovers import save_result_turnovers
from modules.process.modified_list import modified_list


class Test_save_result_turnovers(unittest.TestCase):
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(root_path, "result", "result_process_test.json")
    file_path = Path(file_path)

    def test_save_result_turnovers(self):

        data_list = modified_list()
        data_list.file_path = f"{self.file_path}"

        for i in range(10):
            item_warehouse_turnover = warehouse_turnover_model.create_default(
                turnover=1
            )
            data_list.append(item_warehouse_turnover)


        result = save_result_turnovers.start_process(data_list)

        self.assertEqual(
            result, True
        )

        self.assertEqual(
            self.file_path.is_file(),
            True
        )

        with self.file_path.open("r") as file:
            data = json.load(file)

        for item, new_item in zip(data_list, data):
            item: abstract_model
            self.assertEqual(item.get_dict(), new_item)

