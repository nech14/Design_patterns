
import unittest

from modules.exceptions.argument_exception import argument_exception
from modules.models.organization_model import organization_model
from modules.settings.settings_manager import Settings_manager


class MyTestCase(unittest.TestCase):
    def test__init__(self):
        sm = Settings_manager()
        sm.open("settings1.json", file_path=r"C:\git\Design_patterns\data")

        om = organization_model(sm.settings)

        self.assertEqual(om.score, sm.settings.score)  # add assertion here
        self.assertEqual(om.BIC, sm.settings.BIC)  # add assertion here
        self.assertEqual(om.INN, sm.settings.inn)  # add assertion here

        om.score = sm.settings
        self.assertEqual(om.score, sm.settings.score)
        om.INN = sm.settings
        self.assertEqual(om.BIC, sm.settings.BIC)
        om.BIC = sm.settings
        self.assertEqual(om.INN, sm.settings.inn)
        om.form_ownership = "423"
        self.assertEqual(om.form_ownership, "423")

        with self.assertRaises(argument_exception):
            om = organization_model(setting=41324213)
        with self.assertRaises(argument_exception):
            om.BIC = 123
        with self.assertRaises(argument_exception):
            om.score = 123
        with self.assertRaises(argument_exception):
            om.form_ownership = 123
        with self.assertRaises(argument_exception):
            om.INN = 123


    def test__eq__(self):
        sm = Settings_manager()
        sm.open("settings1.json", file_path=r"C:\git\Design_patterns\data")

        om1 = organization_model(sm.settings)


        sm.open("settings.json", file_path=r"C:\git\Design_patterns\data")

        om2 = organization_model(sm.settings)

        self.assertNotEqual(om1, om2)
        with self.assertRaises(argument_exception):
            result = om1 == "1234"

