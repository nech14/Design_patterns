import os
from copy import copy

from modules.Enums.event_type import event_type
from modules.Enums.transaction_type import enum_transaction_type
from modules.creator_manager import Creator_manager
from modules.exceptions.abstract_logic import abstract_logic
from modules.data_reposity import data_reposity
from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.receipt.receipt_manager import receipt_manager
from modules.models.warehouse_model import warehouse_model
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.service.observer_service import observe_service
from modules.settings.settings_manager import Settings_manager
from modules.settings.settings_base import Settings

"""
Сервис для реализации первого старта приложения
"""
class start_service(abstract_logic):
    __reposity: data_reposity = None
    __settings_manager: Settings_manager = None
    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    __create_manager = Creator_manager()


    def __init__(self, reposity: data_reposity, manager: Settings_manager ) -> None:
        super().__init__()
        if not isinstance(reposity, data_reposity):
            argument_exception(argument_name="reposity")

        if not isinstance(manager, Settings_manager):
            argument_exception(argument_name="manager")

        self.__reposity = reposity
        self.__settings_manager = manager

    """
    Текущие настройки
    """
    @property 
    def settings(self) -> Settings:
        return self.__settings_manager.settings


    def __create_nomenclature(self):
        _list = nomenclature_model.default_nomenclature()

        add_list = []
        for o in _list:
            add_list.append(
                self.__create_manager.add_new_item(o)
            )

        self.__reposity.data[data_reposity.nomenclature_key()] = add_list


    def __create_range(self):
        _list = []
        _list.append(
            self.__create_manager.add_new_item(
                range_model.default_range_grams()
            )
        )
        _list.append(
            self.__create_manager.add_new_item(
                range_model.default_range_pieces()
            )
        )
        _list.append(
            self.__create_manager.add_new_item(
                range_model.default_range_kilogram()
            )
        )

        self.__reposity.data[data_reposity.range_key()] = _list


    """
    Сформировать группы номенклатуры
    """
    def __create_nomenclature_groups(self):
        _list = []
        _list.append(
            self.__create_manager.add_new_item(
                nomenclature_group_model.default_group_cold()
            )
        )
        _list.append(
            self.__create_manager.add_new_item(
                nomenclature_group_model.default_group_source()
            )
        )
        self.__reposity.data[data_reposity.group_key()] = _list


    def __create_receipts(self):
        _list = []
        r_m = receipt_manager(
            nomenclatures= self.__reposity.data[data_reposity.nomenclature_key()],
            ranges= self.__reposity.data[data_reposity.range_key()]
        )
        r_m.read_file(file_path=rf"{self.__root_dir}\Docs\receipt1.md")
        _list.append(
            self.__create_manager.add_new_item(
                copy(r_m.receipt)
            )
        )
        r_m.read_file(file_path=rf"{self.__root_dir}\Docs\receipt2.md")
        _list.append(
            self.__create_manager.add_new_item(
                copy(r_m.receipt)
            )
        )
        self.__reposity.data[data_reposity.receipt_key()] = _list


    def __create_warehouse(self):
        _list = []
        _list.append(
            self.__create_manager.add_new_item(
                warehouse_model.get_base_warehouse("test_warehouse_1", "test_address_1"),
            )
        )
        _list.append(
            self.__create_manager.add_new_item(
                warehouse_model.get_base_warehouse("test_warehouse_2", "test_address_2")
            )
        )

        self.__reposity.data[data_reposity.warehouse_key()] = _list


    def __create_warehouse_transaction(self):
        _list = []

        list_warehouse = self.__reposity.data[data_reposity.warehouse_key()]
        list_nomenclature = self.__reposity.data[data_reposity.nomenclature_key()]

        _list.append(
            self.__create_manager.add_new_item(
                warehouse_transaction_model.get_base_warehouse_transaction(
                    name="test_warehouse_transaction_1",
                    warehouse=list_warehouse[0],
                    nomenclature=list_nomenclature[0],
                    quantity=3,
                    range=list_nomenclature[0].range
                )
            )
        )

        _list.append(
            self.__create_manager.add_new_item(
                warehouse_transaction_model.get_base_warehouse_transaction(
                    name="test_warehouse_transaction_2",
                    warehouse=list_warehouse[1],
                    nomenclature=list_nomenclature[1],
                    range=list_nomenclature[1].range
                )
            )
        )

        _list.append(
            self.__create_manager.add_new_item(
                warehouse_transaction_model.get_base_warehouse_transaction(
                    name="test_warehouse_transaction_2",
                    warehouse=list_warehouse[0],
                    nomenclature=list_nomenclature[0],
                    range=list_nomenclature[1].range,
                    quantity=2,
                    transaction_type=enum_transaction_type.Expense
                )
            )
        )

        self.__reposity.data[data_reposity.warehouse_transaction_key()] = _list




    """
    Первый старт
    """
    def create(self):
        if self.settings.first_start:
            self.__create_nomenclature()
            self.__create_range()
            self.__create_nomenclature_groups()
            self.__create_receipts()
            self.__create_warehouse()
            self.__create_warehouse_transaction()
        else:
            observe_service.raise_event(event=event_type.READ_DATA_REPOSITY, data=self.__reposity)



    """
    Перегрузка абстрактного метода
    """
    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)    


    @property
    def reposity(self):
        return self.__reposity