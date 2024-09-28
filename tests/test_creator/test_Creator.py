import os
import unittest

from modules.creator_manager import Creator_manager
from modules.data_reposity import data_reposity
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.receipt.receipt_model import receipt_model
from modules.reader.format_reading import format_reading
from modules.reader.reader import reader
from modules.reports.format_reporting import format_reporting
from modules.reports.report_manager import Report_manager
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service


class MyTestCase(unittest.TestCase):

    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

    d_r = data_reposity()
    m_s = Settings_manager()
    m_s.open_report_settings(__root_dir + fr'\reports.json')

    s_s = start_service(d_r, m_s)
    s_s.create()

    rep_m = Report_manager()
    rep_m.format = format_reporting.JSON

    keys = list(s_s.reposity.data.keys())

    key = keys[3]

    r = reader({"JSON": "json_reader"})

    def test_json_creator_manager_range_model(self):
        self.rep_m.create(self.s_s.reposity.data[self.keys[1]])

        _path = rf'{self.__root_dir}/reports/{self.keys[1]}'

        os.makedirs(_path, exist_ok=True)
        self.rep_m.save(_path=_path)

        reader_f = self.r.get_reader(format_reading.JSON)
        data = reader_f.read_file(rf"{self.__root_dir}\reports\{self.keys[1]}\report.json")

        c = Creator_manager(data[0])
        c.get_object()
        ob = c.object

        ob_answer =self.s_s.reposity.data[data_reposity.range_key()][0]

        self.assertEqual(
            type(ob),
            range_model
        )

        self.assertEqual(
            ob,
            ob_answer
        )

    def test_json_creator_manager_nomenclature_group_model_model(self):
        self.rep_m.create(self.s_s.reposity.data[self.keys[2]])

        _path = rf'{self.__root_dir}/reports/{self.keys[2]}'

        os.makedirs(_path, exist_ok=True)
        self.rep_m.save(_path=_path)


        reader_f = self.r.get_reader(format_reading.JSON)
        data = reader_f.read_file(rf"{self.__root_dir}\reports\{self.keys[2]}\report.json")

        c = Creator_manager(data[0])
        c.get_object()
        ob = c.object

        ob_answer = self.s_s.reposity.data[data_reposity.group_key()][0]

        self.assertEqual(
            type(ob),
            nomenclature_group_model
        )

        self.assertEqual(
            ob,
            ob_answer
        )


    def test_json_creator_manager_nomenclature_model(self):
        self.rep_m.create(self.s_s.reposity.data[self.keys[0]])

        _path = rf'{self.__root_dir}/reports/{self.keys[0]}'

        os.makedirs(_path, exist_ok=True)
        self.rep_m.save(_path=_path)

        reader_f = self.r.get_reader(format_reading.JSON)
        data = reader_f.read_file(rf"{self.__root_dir}\reports\{self.keys[0]}\report.json")
        c = Creator_manager(data[0])
        c.get_object()
        ob = c.object

        ob_answer = self.s_s.reposity.data[data_reposity.nomenclature_key()][0]

        self.assertEqual(
            type(ob),
            nomenclature_model
        )

        self.assertEqual(
            ob,
            ob_answer
        )




    def test_json_creator_manager_receipt_model(self):
        self.rep_m.create(self.s_s.reposity.data[self.keys[3]])

        _path = rf'{self.__root_dir}/reports/{self.keys[3]}'

        os.makedirs(_path, exist_ok=True)
        self.rep_m.save(_path=_path)

        reader_f = self.r.get_reader(format_reading.JSON)
        data = reader_f.read_file(rf"{self.__root_dir}\reports\{self.keys[3]}\report.json")

        c = Creator_manager(data[0])
        c.get_object()
        ob = c.object

        ob_answer = self.s_s.reposity.data[data_reposity.receipt_key()][0]

        self.assertEqual(
            type(ob),
            receipt_model
        )

        self.assertEqual(
            ob,
            ob_answer
        )
