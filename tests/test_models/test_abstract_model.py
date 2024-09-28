import unittest

from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception
from modules.models.abstract_model import abstract_model
from modules.models.range_model import range_model


class MyTestCase(unittest.TestCase):

    name = "test_name"
    max_len = 50

    def test_name(self):
        rm = range_model(name=self.name)

        self.assertEqual(rm.name, self.name)
        with self.assertRaises(argument_exception):
            rm.name = 1243
        with self.assertRaises(length_exception):
            rm.name = "a"*(self.max_len+1)
        with self.assertRaises(argument_exception):
            rm.unique_code = 421
