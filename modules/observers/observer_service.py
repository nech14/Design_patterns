from modules.Dto.filter_manager import Filter_manager
from modules.Dto.filtration_type import filtration_type
from modules.data_reposity import data_reposity as Data_reposity, data_reposity
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.models.nomenclature_model import nomenclature_model
from modules.observers.abstract_observer import abstract_observer
from modules.process.modified_list import modified_list
from modules.process.processes.abstract_process import abstract_process
from modules.process.processes.read_result_turnovers import read_result_turnovers
from modules.prototype.prototype import prototype


class observer_service(abstract_observer):

    __data_reposity: Data_reposity = None
    __filter_manager: Filter_manager = None
    __prototype: prototype = None
    __check_list = [
        data_reposity.receipt_key()
    ]
    __check_list_save = [
        read_result_turnovers
    ]

    def __init__(self):
        self.__filter_manager = Filter_manager()
        self.__prototype = prototype()


    @property
    def data_reposity(self):
        return self.__data_reposity

    @data_reposity.setter
    def data_reposity(self, value: Data_reposity):
        argument_exception.isinstance(value, Data_reposity)

        self.__data_reposity = value


    def update(self, item: abstract_model):
        argument_exception.isinstance(item, abstract_model)

        for i in self.__check_list:

            item_name_property = f"nomenclature.unique_code"
            _filter = {
                item_name_property: f"{item.unique_code}"
            }

            data = self.__check_items(i, _filter)

            if len(data) > 0:
                return False

        for i in self.__check_list_save:
            i:abstract_process

            _filter = {
                "nomenclature.unique_code": f"{item.unique_code}"
            }

            data = self.__chech_saved_items(i, _filter)

            if len(data) > 0:
                return False


        return True


    def __check_items(self, item, _filter: dict):
        argument_exception.isinstance(_filter, dict)

        self.__filter_manager.update_filter_from_dict(_filter)
        all_data = self.__data_reposity.data[item]

        data = self.__prototype.create(
            all_data,
            self.__filter_manager.filter,
            self.__filter_manager.filter_property,
            filtration_type.LIKE
        ).data

        return data


    def __chech_saved_items(self, process: abstract_process, _filter: dict):
        argument_exception.isinstance(_filter, dict)

        all_data = process.start_process(modified_list())

        self.__filter_manager.update_filter_from_dict(_filter)


        data = self.__prototype.create(
            all_data,
            self.__filter_manager.filter,
            self.__filter_manager.filter_property,
            filtration_type.LIKE
        ).data

        return data
