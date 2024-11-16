import unittest
from copy import copy

from modules.creator_manager import Creator_manager
from modules.data_reposity import data_reposity
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.service.nomenclature_service import nomenclature_service
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service



class TestNomenclatureService(unittest.TestCase):

    manager = Settings_manager()
    manager.open("settings.json", r"..\..\data")
    reposity = data_reposity()
    start = start_service(reposity, manager)
    start.create()


    def test_get_item(self):
        items = self.reposity.data[data_reposity.nomenclature_key()]
        items: list[nomenclature_model]

        service = nomenclature_service()
        service.data_reposity = self.reposity

        for i in range(len(items)):
            self.assertEqual(
                items[i],
                service.get_item(
                    items[i].unique_code
                )
            )

        self.assertNotEqual(
            items[1],
            service.get_item(
                items[0].unique_code
            )
        )


    def test_put_item(self):
        items = self.reposity.data[data_reposity.nomenclature_key()]
        items: list[nomenclature_model]

        service = nomenclature_service()
        service.data_reposity = self.reposity

        new_item = nomenclature_model.create_nomenclature(
            "test_put",
            nomenclature_group_model.default_group_cold(),
            range_model.default_range_grams()
        )

        service.put_item(new_item)

        self.assertEqual(
            items[-1],
            new_item
        )


    def test_path_item(self):
        items = self.reposity.data[data_reposity.nomenclature_key()]
        items: list[nomenclature_model]

        service = nomenclature_service()
        service.data_reposity = self.reposity

        old_item = copy(items[0])

        new_item = nomenclature_model.create_nomenclature(
            "test_path",
            nomenclature_group_model.default_group_cold(),
            range_model.default_range_grams()
        )

        new_item.unique_code = old_item.unique_code
        service.path_item(new_item)

        self.assertEqual(
            items[0].name,
            new_item.name
        )

        self.assertNotEqual(
            items[0].name,
            old_item.name
        )


    def test_delete_item(self):
        items = self.reposity.data[data_reposity.nomenclature_key()]
        items: list[nomenclature_model]

        service = nomenclature_service()
        service.data_reposity = self.reposity

        delete_item = items[0]

        status = service.delete_item(delete_item.unique_code)

        self.assertEqual(
            status,
            True
        )

        for i in items:
            self.assertNotEqual(
                i,
                delete_item
            )

