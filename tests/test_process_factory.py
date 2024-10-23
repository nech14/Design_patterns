import unittest

from modules.data_reposity import data_reposity
from modules.models.warehouse_turnover_model import warehouse_turnover_model
from modules.process_factory import Process_factory
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service


class Test_process_factory(unittest.TestCase):
    manager = Settings_manager()
    manager.open("../settings.json")
    manager.open_report_settings("../reports.json")
    reposity = data_reposity()
    start = start_service(reposity, manager)
    start.create()



    def test_create_warehouse_turnovers(self):
        #preparation
        item_process_factory = Process_factory()

        data = self.reposity.data[self.reposity.warehouse_transaction_key()]
        item_process_factory.data = data

        item_process_factory.create_warehouse_turnovers()

        result = item_process_factory.warehouse_turnovers
        result:list[warehouse_turnover_model]

        #test the creation of a normal quantity
        self.assertEqual(
            len(result),
            2
        )

        #test the work transaction_type
        self.assertEqual(
            result[0].turnover,
            1
        )
