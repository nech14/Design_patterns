import unittest
from datetime import datetime

from modules.exceptions.argument_exception import argument_exception
from modules.exceptions.length_exception import length_exception
from modules.settings.settings_base import Settings


class MyTestCase(unittest.TestCase):
    inn = "123456789012"
    correspondent_account = "12345678901"
    BIC = "123456789"
    type_of_property = "12345"
    score = "12345678901"
    name = "name"

    def test_org_name(self):
        s = Settings()

        s.organization_name = self.name
        self.assertEqual(s.organization_name, self.name)
        with self.assertRaises(argument_exception):
            s.organization_name = 123


    def test_inn(self):
        s = Settings()

        s.inn = self.inn

        self.assertEqual(s.inn, self.inn)
        with self.assertRaises(argument_exception):
            s.inn = 1234
        with self.assertRaises(argument_exception):
            s.inn = "fas"
        with self.assertRaises(length_exception):
            s.inn = "12412"


    def test_correspondent_account(self):
        s = Settings()

        s.correspondent_account = self.correspondent_account

        self.assertEqual(s.correspondent_account, self.correspondent_account)
        with self.assertRaises(argument_exception):
            s.correspondent_account = 124
        with self.assertRaises(length_exception):
            s.correspondent_account = "124"


    def test_BIC(self):
        s = Settings()

        s.BIC = self.BIC

        self.assertEqual(s.BIC, self.BIC)
        with self.assertRaises(argument_exception):
            s.BIC = 124
        with self.assertRaises(length_exception):
            s.BIC = "124"


    def test_type_of_property(self):
        s1 = Settings()

        s1.type_of_property = self.type_of_property

        self.assertEqual(s1.type_of_property, self.type_of_property)
        with self.assertRaises(argument_exception):
            s1.type_of_property = 124
        with self.assertRaises(length_exception):
            s1.type_of_property = "124"


    def test_score(self):
        s = Settings()

        s.score = self.score

        self.assertEqual(s.score, self.score)
        with self.assertRaises(argument_exception):
            s.score = 124
        with self.assertRaises(length_exception):
            s.score = "124"


    def test__str__(self):
        s = Settings()

        s.inn = self.inn
        s.correspondent_account = self.correspondent_account
        s.BIC = self.BIC
        s.type_of_property = self.type_of_property
        s.score = self.score
        s.organization_name = self.name

        self.assertEqual(f"{s}", f"""
        Наименование организации = "{self.name}"
        ИНН = {self.inn}
        Корреспондентский счет = {self.correspondent_account}
        БИК = {self.BIC}
        Вид собственности = {self.type_of_property}
        Счет = {self.score}
        """)


    def test_block_period(self):
        settings = Settings()

        block_period = datetime.now()
        settings.block_period = block_period

        self.assertEqual(block_period, settings.block_period)

        items_not_that_type = [True, 10, 0.2, "bad_item"]
        for i in items_not_that_type:
            with self.assertRaises(argument_exception):
                settings.block_period = i


