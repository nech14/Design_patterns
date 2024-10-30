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
        settings_manager = Settings_manager()
        result = settings_manager.open(self.file_name, file_path=self.file_path, text_encoding='utf-8')
        self.assertEqual(result, True)  # add assertion here
        result = settings_manager.open(self.file_name, file_path=" fdg sdf", text_encoding='utf-8')
        self.assertEqual(result, False)  # add assertion here
        result = settings_manager.open(self.file_name, text_encoding='utf-8')
        self.assertEqual(result, True)  # add assertion here
        with self.assertRaises(argument_exception):
            settings_manager.open(file_name=1231, file_path=self.file_path)
        with self.assertRaises(argument_exception):
            settings_manager.open(file_name=self.file_name, file_path=213)
        with self.assertRaises(argument_exception):
            settings_manager.open(file_name=self.file_name, file_path=self.file_path, text_encoding=321)

        self.assertEqual(isinstance(settings_manager.settings, Settings), True)
        settings_manager.set_exception(ex=self.ex)
        self.assertEqual(settings_manager.error_text, f"Ошибка! Исключение {self.ex}".strip())

        settings_manager.error_text = self.message
        self.assertEqual(settings_manager.is_error, True)




