import unittest

import os
from modules.data_reposity import data_reposity
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service
from modules.reports.format_reporting import format_reporting
from modules.reports.report_manager import Report_manager


class MyTestCase(unittest.TestCase):
    d_r = data_reposity()
    m_s = Settings_manager()

    s_s = start_service(d_r, m_s)
    s_s.create()

    keys = list(s_s.reposity.data.keys())

    rep_m = Report_manager()

    key = keys[3]
    _path = r"C:\git\Design_patterns\reports" + rf'\{key}'

    def test_create_csv(self):

        self.rep_m.format = format_reporting.CSV
        self.rep_m.create(self.s_s.reposity.data[self.key])

        os.makedirs(self._path, exist_ok=True)
        self.rep_m.save(path=self._path)


    def test_create_js(self):

        self.rep_m.format = format_reporting.JSON
        self.rep_m.create(self.s_s.reposity.data[self.key])

        os.makedirs(self._path, exist_ok=True)
        self.rep_m.save(path=self._path)


    def test_create_md(self):

        self.rep_m.format = format_reporting.MARKDOWN
        self.rep_m.create(self.s_s.reposity.data[self.key])

        os.makedirs(self._path, exist_ok=True)
        self.rep_m.save(path=self._path)


    def test_create_xml(self):

        self.rep_m.format = format_reporting.XML
        self.rep_m.create(self.s_s.reposity.data[self.key])

        os.makedirs(self._path, exist_ok=True)
        self.rep_m.save(path=self._path)


    def test_create_rtf(self):

        self.rep_m.format = format_reporting.RTF
        self.rep_m.create(self.s_s.reposity.data[self.key])

        os.makedirs(self._path, exist_ok=True)
        self.rep_m.save(path=self._path)