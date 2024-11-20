import unittest

from modules.data_reposity import data_reposity
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.observers.observer_update_nomenclature import observer_update_nomenclature
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service


class TestObserverService(unittest.TestCase):

    manager = Settings_manager()
    manager.open("settings.json", r"..\..\data")
    reposity = data_reposity()
    start = start_service(reposity, manager)
    start.create()


    def test_update(self):

        observer = observer_update_nomenclature()
        observer.data_reposity = self.reposity

        list_nomenclature = self.reposity.data[data_reposity.nomenclature_key()]


        self.assertEqual(
            observer.update(
                list_nomenclature[0]
            ),
            False
        )


        new_nomenclature = nomenclature_model.create_nomenclature(
            "test",
            nomenclature_group_model.default_group_cold(),
            range_model.default_range_grams()
        )

        self.assertEqual(
            observer.update(
                new_nomenclature
            ),
            True
        )

