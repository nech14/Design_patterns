import unittest

from modules.Enums.transaction_type import enum_transaction_type
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.process.list_processes import list_processes
from modules.process.process_factory import Process_factory


class Test_create_warehouse_turnovers(unittest.TestCase):

    def test_create_warehouse_turnovers(self):

        data = []
        for i in range(20):
            item = warehouse_transaction_model.get_base_warehouse_transaction()
            data.append(item)

        process_factory = Process_factory()

        result = process_factory.start_process(
            data,
            list_processes.create_warehouse_turnovers.name
        )

        self.assertEqual(
            len(result),
            1
        )
        self.assertEqual(
            result[0].turnover,
            20
        )

        for i in range(10):
            item = warehouse_transaction_model.get_base_warehouse_transaction(
                transaction_type=enum_transaction_type.Expense
            )
            data.append(item)

        result = process_factory.start_process(
            data,
            list_processes.create_warehouse_turnovers.name
        )

        self.assertEqual(
            len(result),
            1
        )
        self.assertEqual(
            result[0].turnover,
            10
        )

