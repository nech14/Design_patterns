import unittest
import requests
import json
import jsonpickle

from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.warehouse_model import warehouse_model

# URL вашего Flask приложения
url = "http://127.0.0.1:8080/api"

class Test_api(unittest.TestCase):


    def test_warehouse_transaction(self):
        new_url = url + "/api/warehouse_transaction/LIKE"
        data = {}

        item_warehouse = warehouse_model.get_base_warehouse(name="", address="test_address", unique_code="")
        item_nomenclature = nomenclature_model.create_nomenclature(
            "",
            nomenclature_group_model.default_group_source(),
            range_model.default_range_grams()
        )

        data["warehouse"] = json.loads(jsonpickle.encode(item_warehouse))
        data["nomenclature"] = json.loads(jsonpickle.encode(item_nomenclature))

        # Отправка POST-запроса
        response = requests.post(new_url, json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.text) > 0,
            True
        )


    def test_warehouse_transaction_bad_filter(self):
        filter_type = "LIK"
        new_url = url + f"/api/warehouse_transaction/{filter_type}"
        data = {}

        item_warehouse = warehouse_model.get_base_warehouse(name="", address="", unique_code="")
        item_nomenclature = nomenclature_model.create_nomenclature(
            "",
            nomenclature_group_model.default_group_source(),
            range_model.default_range_grams()
        )

        data["warehouse"] = json.loads(jsonpickle.encode(item_warehouse))
        data["nomenclature"] = json.loads(jsonpickle.encode(item_nomenclature))

        # Отправка POST-запроса
        response = requests.post(new_url, json=data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.text,
            f"such a filter({filter_type}) is not implemented"
        )



    def test_warehouse_turnover(self):
        new_url = url + "/api/warehouse_turnover/EQUALS"
        data = {}

        item_warehouse = warehouse_model.get_base_warehouse(name="", address="", unique_code="")
        item_nomenclature = nomenclature_model.create_nomenclature(
            "",
            nomenclature_group_model.default_group_source(),
            range_model.default_range_grams()
        )

        data["warehouse"] = json.loads(jsonpickle.encode(item_warehouse))
        data["nomenclature"] = json.loads(jsonpickle.encode(item_nomenclature))


        # Отправка POST-запроса
        response = requests.post(new_url, json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.text) > 0,
            True
        )

    def test_warehouse_turnover_bad_filter(self):
        filter_type = "EQUA"
        new_url = url + f"/api/warehouse_turnover/{filter_type}"
        data = {}

        item_warehouse = warehouse_model.get_base_warehouse(name="", address="", unique_code="")
        item_nomenclature = nomenclature_model.create_nomenclature(
            "",
            nomenclature_group_model.default_group_source(),
            range_model.default_range_grams()
        )

        data["warehouse"] = json.loads(jsonpickle.encode(item_warehouse))
        data["nomenclature"] = json.loads(jsonpickle.encode(item_nomenclature))

        # Отправка POST-запроса
        response = requests.post(new_url, json=data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.text,
            f"such a filter({filter_type}) is not implemented"
        )

