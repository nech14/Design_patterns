import os
import unittest

from modules.reader.format_reading import format_reading
from modules.reader.reader import reader




class MyTestCase(unittest.TestCase):

    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))


    def test_json_reader(self):
        r = reader({"JSON" : "json_reader"})

        reader_f = r.get_reader(format_reading.JSON)
        _dict = reader_f.read_file(rf"{self.__root_dir}\reports\range\report.js")[0]


        answer_dict =  {
            '__class__': 'range_model',
            'name': 'гр',
            'model_unique_code': '400b20fa-ae68-4a09-8e87-e50b83df0e35',
            'conversion_factor': 1,
            'base_unit_measurement': None
        }

        self.assertEqual(
            _dict,
            answer_dict
        )



