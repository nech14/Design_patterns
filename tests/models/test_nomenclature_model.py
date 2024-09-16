
import unittest

from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.nomenclature_model import nomenciature_model
from modules.models.range_model import range_model


class MyTestCase(unittest.TestCase):
    def test_group(self):
        nm = nomenciature_model()
        ngm = nomenclature_group_model()

        nm.group = ngm
        self.assertEqual(nm.group, ngm)
        with self.assertRaises(argument_exception):
            nm.group = 123


    def test_range(self):
        nm = nomenciature_model()
        rm = range_model("кг")

        nm.range = rm
        self.assertEqual(nm.range, rm)
        with self.assertRaises(argument_exception):
            nm.range = 123


    def test__eq__(self):
        nm1 = nomenciature_model()
        nm2 = nomenciature_model()

        nm1.unique_code = "123"
        nm2.unique_code = "321"

        self.assertNotEqual(nm1, nm2)
        with self.assertRaises(argument_exception):
            result = nm1 == 124
