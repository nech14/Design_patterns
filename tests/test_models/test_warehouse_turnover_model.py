import unittest

from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.warehouse_model import warehouse_model
from modules.models.warehouse_turnover_model import warehouse_turnover_model


class Test_warehouse_turnover_model(unittest.TestCase):

    def test_create(self):
        #preparation
        item_warehouse_turnover_model = warehouse_turnover_model()

        #test warehouse_model
        item_warehouse_model = warehouse_model()
        item_warehouse_turnover_model.warehouse = item_warehouse_model
        self.assertEqual(item_warehouse_turnover_model.warehouse, item_warehouse_model)

        items_not_that_type = [True, 10, 0.2, "bad_item"]
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                item_warehouse_turnover_model.warehouse = i


        #test turnover
        item_turnover = 10
        item_warehouse_turnover_model.turnover = item_turnover
        self.assertEqual(item_warehouse_turnover_model.turnover, item_turnover)

        items_not_that_type = [True, 0.2, "bad_item"]
        print(isinstance(False, int))
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                item_warehouse_turnover_model.turnover = i


        #test nomenclature
        item_nomenclature = nomenclature_model()
        item_warehouse_turnover_model.nomenclature = item_nomenclature
        self.assertEqual(item_warehouse_turnover_model.nomenclature, item_nomenclature)

        items_not_that_type = [True, 10, 0.2, "bad_item"]
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                item_warehouse_turnover_model.nomenclature = i


        #test range
        item_range = range_model("test_range")
        item_warehouse_turnover_model.range = item_range
        self.assertEqual(item_warehouse_turnover_model.range, item_range)

        items_not_that_type = [True, 10, 0.2, "bad_item"]
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                item_warehouse_turnover_model.range = i


        #test equality
        item2_warehouse_turnover_model = warehouse_model()
        self.assertNotEqual(
            item_warehouse_turnover_model,
            item2_warehouse_turnover_model
        )
