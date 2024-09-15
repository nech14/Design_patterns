import unittest
from idlelib.iomenu import encoding

from modules.exceptions.argument_exception import argument_exception
from modules.settings.settings_base import Settings
from modules.settings.settings_manager import Settings_manager


class MyTestCase(unittest.TestCase):

    file_name = "settings1.json"
    file_path = r"C:\git\Design_patterns\data"
    ex = argument_exception()
    message = "test"

    def test_open(self):
        s = Settings_manager()
        result = s.open(self.file_name, file_path=self.file_path, text_encoding='utf-8')
        self.assertEqual(result, True)  # add assertion here
        result = s.open(self.file_name, file_path=" fdg sdf", text_encoding='utf-8')
        self.assertEqual(result, False)  # add assertion here
        result = s.open(self.file_name, text_encoding='utf-8')
        self.assertEqual(result, True)  # add assertion here
        with self.assertRaises(argument_exception):
            s.open(file_name=1231, file_path=self.file_path)
        with self.assertRaises(argument_exception):
            s.open(file_name=self.file_name, file_path=213)
        with self.assertRaises(argument_exception):
            s.open(file_name=self.file_name, file_path=self.file_path, text_encoding=321)

        self.assertEqual(isinstance(s.settings, Settings), True)
        s.set_exception(ex=self.ex)
        self.assertEqual(s.error_text, f"Ошибка! Исключение {self.ex}".strip())

        s.error_text = self.message
        self.assertEqual(s.is_error, True)


