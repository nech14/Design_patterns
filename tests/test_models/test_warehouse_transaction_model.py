import unittest
from datetime import datetime

from modules.Enums.transaction_type import transaction_type
from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.warehouse_model import warehouse_model
from modules.models.warehouse_transaction_model import warehouse_transaction_model


class Test_warehouse_transaction_model(unittest.TestCase):

    def test_create(self):
        #preparation
        item_warehouse_transaction_model = warehouse_transaction_model()

        #test warehouse
        item_warehouse = warehouse_model()
        item_warehouse_transaction_model.warehouse = item_warehouse
        self.assertEqual(
            item_warehouse_transaction_model.warehouse,
            item_warehouse,
            "problem with warehouse"
        )

        items_not_that_type = [True, 10, 0.2, "bad_item"]
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                item_warehouse_transaction_model.warehouse = i


        #test nomenclature
        item_nomenclature = nomenclature_model()
        item_warehouse_transaction_model.nomenclature = item_nomenclature
        self.assertEqual(
            item_warehouse_transaction_model.nomenclature,
            item_nomenclature,
            "problem with nomenclature"
        )

        items_not_that_type = [True, 10, 0.2, "bad_item"]
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                item_warehouse_transaction_model.nomenclature = i


        #test quantity
        item_quantity = 10
        item_warehouse_transaction_model.quantity = item_quantity
        self.assertEqual(
            item_warehouse_transaction_model.quantity,
            item_quantity,
            "problem with quantity"
        )

        items_not_that_type = [True, 0.2, "bad_item"]
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                item_warehouse_transaction_model.quantity = i


        #test transaction_type
        item_transaction_type = transaction_type.Income
        item_warehouse_transaction_model.transaction_type = item_transaction_type
        self.assertEqual(
            item_warehouse_transaction_model.transaction_type,
            item_transaction_type,
            "problem with transaction_type"
        )

        items_not_that_type = [True, 10, 0.2, "bad_item"]
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                item_warehouse_transaction_model.transaction_type = i


        #test range
        item_range = range_model("test_range")
        item_warehouse_transaction_model.range = item_range
        self.assertEqual(
            item_warehouse_transaction_model.range,
            item_range,
            "problem with range"
        )

        items_not_that_type = [True, 10, 0.2, "bad_item"]
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                item_warehouse_transaction_model.range = i


        #test period
        item_period = datetime.now()
        item_warehouse_transaction_model.period = item_period
        self.assertEqual(
            item_warehouse_transaction_model.period,
            item_period,
            "problem with period"
        )

        items_not_that_type = [True, 10, 0.2, "bad_item"]
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                item_warehouse_transaction_model.period = i
