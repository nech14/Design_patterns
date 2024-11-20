import os
import unittest
from copy import copy

from modules.Enums.event_type import event_type
from modules.data_reposity import data_reposity
from modules.service.data_service import Data_service
from modules.service.observer_service import observe_service
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service


class Test_data_service(unittest.TestCase):

    def test_save_data(self):
        manager = Settings_manager()
        manager.open("settings.json", "../../data")
        manager.open_report_settings("../../reports.json")
        reposity = data_reposity()
        start = start_service(reposity, manager)
        start.create()

        data_service = Data_service()
        data_service.file_path = "../../result/data_reposity.json"

        observe_service.raise_event(event=event_type.SAVE_DATA_REPOSITY, data=reposity)

        self.assertEqual(
            os.path.exists(data_service.file_path),
            True
        )


    def test_read_data(self):
        manager = Settings_manager()
        manager.open("settings.json", "../../data")
        manager.open_report_settings("../../reports.json")
        reposity = data_reposity()
        start = start_service(reposity, manager)
        start.create()

        data_service = Data_service()
        data_service.file_path = "../../result/data_reposity.json"

        observe_service.raise_event(event=event_type.SAVE_DATA_REPOSITY, data=reposity)

        self.assertEqual(
            os.path.exists(data_service.file_path),
            True
        )

        last_data = copy(reposity.data)

        observe_service.raise_event(event_type.READ_DATA_REPOSITY, data=reposity)

        self.assertEqual(
            last_data,
            reposity.data
        )

        self.assertEqual(
            last_data is reposity.data,
            False
        )