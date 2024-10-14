import unittest

from modules.Dto.filter_manager import Filter_manager
from modules.Dto.filtration_type import filtration_type
from modules.data_key import data_key
from modules.data_reposity import data_reposity
from modules.prototype.prototype import prototype
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service


class MyTestCase(unittest.TestCase):
    manager = Settings_manager()
    manager.open("../settings.json")
    manager.open_report_settings("../reports.json")
    reposity = data_reposity()
    start = start_service(reposity, manager)
    start.create()


    def test_create(self):
        prototype_obj = prototype()

        filter_dict = {
            "model_unique_code": "",
            'name': 'Пшеничная мука'
        }

        filter_manager = Filter_manager()
        filter_manager.update_filter_from_dict(filter_dict)

        data = self.reposity.data[data_key.nomenclature_model.value]

        new_data = prototype_obj.create(
            data,
            filter_manager.filter,
            filter_manager.filter_property,
            filtration_type.EQUALS
        ).data

        self.assertEqual(
            len(new_data),
            1
        )

        self.assertEqual(
            new_data[0],
            data[0]
        )