
import unittest

from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model


class MyTestCase(unittest.TestCase):
    def test_group(self):
        nm = nomenclature_model()
        ngm = nomenclature_group_model()

        nm.group = ngm
        self.assertEqual(nm.group, ngm)
        with self.assertRaises(argument_exception):
            nm.group = 123


    def test_range(self):
        nm = nomenclature_model()
        rm = range_model("кг")

        nm.range = rm
        self.assertEqual(nm.range, rm)
        with self.assertRaises(argument_exception):
            nm.range = 123


    def test__eq__(self):
        nm1 = nomenclature_model()
        nm2 = nomenclature_model()

        nm1.unique_code = "123"
        nm2.unique_code = "321"

        self.assertNotEqual(nm1, nm2)
        with self.assertRaises(argument_exception):
            result = nm1 == 124


    def test_create_nomenclature(self):
        base_nomenclatures_name = ["Пшеничная мука", "Сахар"]
        base_nomenclatures_groupe = [nomenclature_group_model.default_group_source() for i in range(2)]
        base_nomenclatures_range = [range_model("гр", 1), range_model("гр", 1)]

        with self.assertRaises(argument_exception):
            nm = nomenclature_model.crate_nomenclature(
                [1],
                base_nomenclatures_groupe,
                base_nomenclatures_range
            )

        with self.assertRaises(argument_exception):
            nm = nomenclature_model.crate_nomenclature(
                base_nomenclatures_name,
                [""],
                base_nomenclatures_range
            )

        with self.assertRaises(argument_exception):
            nm = nomenclature_model.crate_nomenclature(
                base_nomenclatures_name,
                base_nomenclatures_groupe,
                [""]
            )

        nm = nomenclature_model.crate_nomenclature(
            base_nomenclatures_name,
            base_nomenclatures_groupe,
            base_nomenclatures_range
        )

        self.assertNotEqual(nm, None)


