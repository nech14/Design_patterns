
import unittest
import uuid

from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_group_model import nomenclature_group_model


class MyTestCase(unittest.TestCase):

    def test__eqe__(self):
        ngm = nomenclature_group_model()

        with self.assertRaises(argument_exception):
            result = ngm == str("214")


    def test_default_group_cold(self):
        group = nomenclature_group_model.default_group_cold()

        self.assertEqual(group.name, "Заморозка")


