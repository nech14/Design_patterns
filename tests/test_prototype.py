import unittest
from datetime import datetime

from modules.Dto.filter_manager import Filter_manager
from modules.Dto.filtration_type import filtration_type
from modules.Enums.data_key import data_key
from modules.data_reposity import data_reposity
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.prototype.prototype import prototype
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service


class Test_prototype(unittest.TestCase):
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


    def test_filter_INTERVAL(self):
        # preparation
        item_prototype = prototype()

        data = []

        item1_warehouse_transaction = warehouse_transaction_model.get_base_warehouse_transaction(
            name="test_1_warehouse_transaction",
            period=datetime(2024, 10, 20)
        )
        data.append(item1_warehouse_transaction)

        item2_warehouse_transaction = warehouse_transaction_model.get_base_warehouse_transaction(
            name="test_2_warehouse_transaction",
            period=datetime(2024, 10, 22)
        )
        data.append(item2_warehouse_transaction)

        #getting the whole date
        filter_dict = {
            "model_unique_code": "",
            "period": [
                datetime(2024, 10, 20),
                datetime(2024, 10, 22)
            ]
        }

        filter_manager = Filter_manager()
        filter_manager.update_filter_from_dict(filter_dict)

        new_data = item_prototype.create(
            data,
            filter_manager.filter,
            filter_manager.filter_property,
            filtration_type.INTERVAL
        ).data

        self.assertEqual(len(new_data), 2)
        self.assertEqual(
            new_data[0],
            item1_warehouse_transaction
        )
        self.assertEqual(
            new_data[1],
            item2_warehouse_transaction
        )


        #new filter
        filter_dict = {
            "model_unique_code": "",
            "period": [
                datetime(2024, 10, 22),
                datetime(2024, 10, 23)
            ]
        }
        filter_manager.update_filter_from_dict(filter_dict)

        new_data = item_prototype.create(
            data,
            filter_manager.filter,
            filter_manager.filter_property,
            filtration_type.INTERVAL
        ).data

        self.assertEqual(len(new_data), 1)
        self.assertEqual(
            new_data[0],
            item2_warehouse_transaction
        )
