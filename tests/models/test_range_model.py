
import unittest

from modules.exceptions.argument_exception import argument_exception
from modules.models.range_model import range_model


class MyTestCase(unittest.TestCase):
    conversion_factor = 1000
    name = "кг"
    base_unit_measurement = range_model("грамм", 1)


    def test__init__(self):

        rm = range_model(self.name, conversion_factor=self.conversion_factor, base_unit_measurement=self.base_unit_measurement)

        self.assertEqual(rm.conversion_factor, self.conversion_factor)
        rm.conversion_factor = self.conversion_factor
        self.assertEqual(rm.conversion_factor, self.conversion_factor)
        rm.base_unit_measurement = self.base_unit_measurement
        self.assertEqual(rm.base_unit_measurement, self.base_unit_measurement)


        with self.assertRaises(argument_exception):
            range_model(self.name, "fsadfa", base_unit_measurement=self.base_unit_measurement)
        with self.assertRaises(argument_exception):
            range_model(self.name, conversion_factor=self.conversion_factor, base_unit_measurement=214)
        with self.assertRaises(argument_exception):
            range_model(124, conversion_factor=self.conversion_factor, base_unit_measurement=self.base_unit_measurement)
        with self.assertRaises(argument_exception):
            rm.base_unit_measurement = 123
        with self.assertRaises(argument_exception):
            rm.conversion_factor = "sdgasd"
