import unittest

from attr.validators import max_len

from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception
from modules.models.abstract_reference import abstract_reference


class MyTestCase(unittest.TestCase):

    name = "test_name"
    max_len = 50

    def test_name(self):
        a = abstract_reference()
        a.name = self.name

        self.assertEqual(a.name, self.name)
        with self.assertRaises(argument_exception):
            a.name = 1243
        with self.assertRaises(length_exception):
            a.name = "a"*(self.max_len+1)
