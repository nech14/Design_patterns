import unittest
from datetime import datetime

from modules.Enums.transaction_type import enum_transaction_type
from modules.models.TBS_model import TBS_model
from modules.models.warehouse_model import warehouse_model
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.process.list_processes import list_processes
from modules.process.modified_list import modified_list
from modules.process.process_factory import Process_factory


class Test_create_TBS(unittest.TestCase):


    def test_create_TBS(self):

        data_transaction = []
        incomes = []
        expenses = []
        for y in range(3):
            for i in range(10):
                item = warehouse_transaction_model.get_base_warehouse_transaction(
                        name=f"test_transaction_Income_{i}",
                        quantity=i,
                        transaction_type=enum_transaction_type.Income,
                        period=datetime(year=2010+y, month=1, day=1)
                    )
                data_transaction.append(item)
                incomes.append(item)


            for i in range(5):
                item =  warehouse_transaction_model.get_base_warehouse_transaction(
                        name=f"test_transaction_Expense_{i}",
                        quantity=i,
                        transaction_type=enum_transaction_type.Expense,
                        period=datetime(year=2010+y, month=1, day=1)
                    )
                data_transaction.append(item)
                expenses.append(item)

        data_transaction = modified_list(data_transaction)
        data_transaction.date = datetime(year=2011, month=1, day=1)

        process_factory = Process_factory()
        result: TBS_model = process_factory.start_process(data_transaction, list_processes.create_TBS.name)



        self.assertEqual(
            result.incomes,
            incomes
        )

        self.assertEqual(
            result.expenses,
            expenses
        )

        self.assertEqual(
            len(result.opening_remainder),
            1
        )
        self.assertEqual(
            len(result.remainder),
            1
        )




