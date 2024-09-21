import os
import unittest

from setuptools.sandbox import save_path

from modules.exceptions.argument_exception import argument_exception
from modules.models.receipt_model import receipt_model

class MyTestCase(unittest.TestCase):

    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

    def test_read_file(self):
        receipt = receipt_model()

        with self.assertRaises(argument_exception):
            receipt.read_file(file_path=123)

        receipt.read_file(file_path=fr"{self.__root_dir}/Docs/receipt1.md")

        path_save = fr"{self.__root_dir}/Docs/receipt_test.md"
        receipt.save_in_file(file_path=path_save)
        self.assertEqual(os.path.isfile(path_save), True)

        if os.path.isfile(path_save):
            receipt_test = receipt_model()
            receipt_test.read_file(file_path=path_save)

            self.assertEqual(receipt, receipt_test)

            self.assertEqual(receipt.name, receipt_test.name)
            self.assertEqual(receipt.portions, receipt_test.portions)
            self.assertEqual(receipt.cooking_time, receipt_test.cooking_time)
            self.assertEqual(receipt.steps, receipt_test.steps)
            self.assertEqual(receipt.ingredients, receipt_test.ingredients)

            os.remove(path_save)

