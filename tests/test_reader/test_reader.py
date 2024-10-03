import os
import unittest

from modules.models.range_model import range_model
from modules.reader.format_reading import format_reading
from modules.reader.reader import reader
from modules.reports.format_reporting import format_reporting
from modules.reports.report_manager import Report_manager


class MyTestCase(unittest.TestCase):

    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    _path = rf"{__root_dir}\reports\range"

    def test_json_reader(self):
        rep_m = Report_manager()
        rep_m.format = format_reporting.JSON
        data_reports = [
            range_model.default_range_grams()
        ]
        rep_m.create(data_reports)
        rep_m.save(_path= rf"{self._path}")

        r = reader({"JSON" : "json_reader"})

        reader_f = r.get_reader(format_reading.JSON)
        _dict = reader_f.read_file(rf"{self._path}\report.json")[0]


        self.assertEqual(
            _dict,
            data_reports[0].get_dict()
        )



