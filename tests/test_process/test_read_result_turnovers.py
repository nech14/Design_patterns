import os
import unittest
from pathlib import Path

from modules.models.warehouse_turnover_model import warehouse_turnover_model
from modules.process.processes.read_result_turnovers import read_result_turnovers
from modules.process.processes.save_result_turnovers import save_result_turnovers
from modules.process.modified_list import modified_list


class Test_read_result_turnovers(unittest.TestCase):

    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(root_path, "result", "result_process_test.json")
    file_path = Path(file_path)

    def test_read_result_turnovers(self):

        data_list = modified_list()
        data_list.file_path = f"{self.file_path}"

        for i in range(10):
            item_warehouse_turnover = warehouse_turnover_model.create_default()
            data_list.append(item_warehouse_turnover)

        result = save_result_turnovers.start_process(data_list)

        self.assertEqual(
            result,
            True
        )

        data = read_result_turnovers.start_process(data_list)

        self.assertEqual(
            data_list,
            data
        )

