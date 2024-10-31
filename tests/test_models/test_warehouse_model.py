import unittest

from modules.models.warehouse_model import warehouse_model


class Test_warehouse_model(unittest.TestCase):

    def test_create(self):

        item1 = warehouse_model()
        item1.address = "test1"

        self.assertEqual(item1.address, "test1")

        item2 = warehouse_model()
        item2.address = "test1"

        self.assertNotEqual(item1, item2)






