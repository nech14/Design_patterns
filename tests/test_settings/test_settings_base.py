import unittest
from modules.settings.settings_base import Settings


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Settings()
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
