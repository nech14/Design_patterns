import os
import unittest
from copy import copy

from modules.exceptions.argument_exception import argument_exception
from modules.models.receipt.receipt_manager import receipt_manager
from modules.models.receipt.receipt_model import receipt_model

class MyTestCase(unittest.TestCase):

    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

    def test_read_file(self):
        receipt_m = receipt_manager()

        with self.assertRaises(argument_exception):
            receipt_m.receipt = 124


        with self.assertRaises(argument_exception):
            receipt_m.read_file(file_path=123)


        receipt_m.read_file(file_path=fr"{self.__root_dir}/Docs/receipt1.md")

        receipt = copy(receipt_m.receipt)

        path_save = fr"{self.__root_dir}/Docs/receipt_test.md"
        receipt_m.save_in_file(file_path=path_save)
        self.assertEqual(os.path.isfile(path_save), True)

        if os.path.isfile(path_save):
            receipt_test = copy(receipt_m.receipt)
            receipt_m.receipt = receipt
            receipt_m.read_file(file_path=path_save)

            self.assertEqual(receipt, receipt_test)

            self.assertEqual(receipt.name, receipt_test.name)
            self.assertEqual(receipt.portions, receipt_test.portions)
            self.assertEqual(receipt.cooking_time, receipt_test.cooking_time)
            self.assertEqual(receipt.steps, receipt_test.steps)
            self.assertEqual(receipt.ingredients, receipt_test.ingredients)

            os.remove(path_save)

