import unittest

import os
from datetime import datetime

from modules.Enums.transaction_type import enum_transaction_type
from modules.data_reposity import data_reposity
from modules.models.TBS_model import TBS_model
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.process.list_processes import list_processes
from modules.process.modified_list import modified_list
from modules.process.process_factory import Process_factory
from modules.reports.report_factory import report_factory
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service
from modules.reports.format_reporting import format_reporting
from modules.reports.report_manager import Report_manager


class MyTestCase(unittest.TestCase):
    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

    d_r = data_reposity()
    m_s = Settings_manager()
    m_s.open_report_settings(__root_dir+fr'\reports.json')

    s_s = start_service(d_r, m_s)
    s_s.create()

    keys = list(s_s.reposity.data.keys())

    rep_m = Report_manager()

    key = keys[0]
    _path = rf'{__root_dir}/reports/{key}'

    def test_create_csv(self):

        self.rep_m.format = format_reporting.CSV
        self.rep_m.create(self.s_s.reposity.data[self.key])

        os.makedirs(self._path, exist_ok=True)
        self.rep_m.save(_path=self._path)


    def test_create_json(self):
        # report_factory(self.m_s.report_settings)
        self.rep_m.format = format_reporting.JSON
        self.rep_m.create(self.s_s.reposity.data[self.key])

        os.makedirs(self._path, exist_ok=True)
        self.rep_m.save(_path=self._path)


    def test_create_md(self):

        self.rep_m.format = format_reporting.MARKDOWN
        self.rep_m.create(self.s_s.reposity.data[self.key])

        os.makedirs(self._path, exist_ok=True)
        self.rep_m.save(_path=self._path)


    def test_create_xml(self):

        self.rep_m.format = format_reporting.XML
        self.rep_m.create(self.s_s.reposity.data[self.key])

        os.makedirs(self._path, exist_ok=True)
        self.rep_m.save(_path=self._path)


    def test_create_rtf(self):

        self.rep_m.format = format_reporting.RTF
        self.rep_m.create(self.s_s.reposity.data[self.key])

        os.makedirs(self._path, exist_ok=True)
        self.rep_m.save(_path=self._path)

    def test_create_TBS(self):
        data_transaction = []
        incomes = []
        expenses = []
        for y in range(3):
            for i in range(10):
                item = warehouse_transaction_model.get_base_warehouse_transaction(
                    name=f"test_transaction_Income_{i}",
                    quantity=i,
                    transaction_type=enum_transaction_type.Income,
                    period=datetime(year=2010 + y, month=1, day=1)
                )
                data_transaction.append(item)
                incomes.append(item)

            for i in range(5):
                item = warehouse_transaction_model.get_base_warehouse_transaction(
                    name=f"test_transaction_Expense_{i}",
                    quantity=i,
                    transaction_type=enum_transaction_type.Expense,
                    period=datetime(year=2010 + y, month=1, day=1)
                )
                data_transaction.append(item)
                expenses.append(item)

        data_transaction = modified_list(data_transaction)
        data_transaction.date = datetime(year=2011, month=1, day=1)

        process_factory = Process_factory()
        result: TBS_model = process_factory.start_process(data_transaction, list_processes.create_TBS.name)

        self.rep_m.format = format_reporting.JSON
        self.rep_m.create([result.get_dict()])

        _path = rf'{self.__root_dir}/reports/TBS'
        os.makedirs(_path, exist_ok=True)
        self.rep_m.save(_path=_path)

