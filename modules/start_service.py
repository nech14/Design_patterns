import os

from modules.exceptions.abstract_logic import abstract_logic
from modules.data_reposity import data_reposity
from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_group_model import nomenclature_group_model
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.receipt_model import receipt_model
from modules.settings.settings_manager import Settings_manager
from modules.settings.settings_base import Settings

"""
Сервис для реализации первого старта приложения
"""
class start_service(abstract_logic):
    __reposity: data_reposity = None
    __settings_manager: Settings_manager = None
    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    __base_nomenclatures_name = ["Пшеничная мука", "Сахар", "Сливочное масло", "Яйца", "Ванилин(щепотка)"]
    __base_nomenclatures_groupe = [nomenclature_group_model.default_group_source() for i in range(5)]
    __base_nomenclatures_range = [range_model("гр", 1), range_model("гр", 1),
                                  range_model("гр", 1), range_model("шт", 1),
                                  range_model("гр", 1)]


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
        _list = nomenclature_model.crate_nomenclature(
            self.__base_nomenclatures_name,
            self.__base_nomenclatures_groupe,
            self.__base_nomenclatures_range
        )

        self.__reposity.data[data_reposity.nomenclature_key()] = _list


    def __create_range(self):
        _list = []
        _list.append(range_model.default_range_grams())
        _list.append(range_model.default_range_pieces())

        self.__reposity.data[data_reposity.range_key()] = _list


    """
    Сформировать группы номенклатуры
    """
    def __create_nomenclature_groups(self):
        _list = []
        _list.append(nomenclature_group_model.default_group_cold())
        _list.append( nomenclature_group_model.default_group_source())
        self.__reposity.data[data_reposity.group_key()] = _list


    def __create_receipts(self):
        _list = []
        _list.append(receipt_model().read_file(file_path=rf"{self.__root_dir}\Docs\receipt1.md"))
        _list.append(receipt_model().read_file(file_path=rf"{self.__root_dir}\Docs\receipt2.md"))
        self.__reposity.data[data_reposity.receipt_key()] = _list


    """
    Первый старт
    """
    def create(self):
        self.__create_nomenclature()
        self.__create_range()
        self.__create_nomenclature_groups()
        self.__create_receipts()



    """
    Перегрузка абстрактного метода
    """
    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)    

