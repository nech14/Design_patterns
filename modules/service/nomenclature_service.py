
from modules.Dto.filter_manager import Filter_manager
from modules.Dto.filtration_type import filtration_type
from modules.creator_manager import Creator_manager
from modules.data_reposity import data_reposity as Data_reposity
from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_model import nomenclature_model
from modules.models.warehouse_turnover_model import warehouse_turnover_model
from modules.process.modified_list import modified_list
from modules.process.processes.read_result_turnovers import read_result_turnovers
from modules.process.processes.save_result_turnovers import save_result_turnovers
from modules.prototype.prototype import prototype
from modules.service.service_with_subscription import service_with_subscription


class nomenclature_service(service_with_subscription):

    __data_reposity: Data_reposity = []
    __data_key: str = Data_reposity.nomenclature_key()
    __filter_manager: Filter_manager = None
    __prototype:prototype = None
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

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


    def get_item(self, ID: str):
        argument_exception.isinstance(ID, str)

        _filter = {
            'unique_code': f"{ID}"
        }

        list_with_item = self.__get_filtered_data(_filter)

        if len(list_with_item) == 0:
            return None

        return list_with_item[0]


    def put_item(self, item: nomenclature_model):
        argument_exception.isinstance(item, nomenclature_model)

        try:
            data: list = self.__data_reposity.data[self.__data_key]
            data.append(
                Creator_manager().add_new_item(item)
            )

            return True
        except Exception as e:
            return False



    def path_item(self, item: nomenclature_model):
        argument_exception.isinstance(item, nomenclature_model)


        warehouse_turnover_data = read_result_turnovers.start_process()


        _filter = {
            'unique_code': f"{item.unique_code}"
        }


        list_with_item = self.__get_filtered_data(_filter)


        if len(list_with_item) == 0:
            return False

        Creator_manager().add_new_item(item)

        save_result_turnovers.start_process(
            modified_list(warehouse_turnover_data)
        )

        return True



    def delete_item(self, ID: str):
        argument_exception.isinstance(ID, str)

        _filter = {
            'unique_code': f"{ID}"
        }

        list_with_item = self.__get_filtered_data(_filter)

        if len(list_with_item) == 0:
            return None

        item = list_with_item[0]

        if self._notify_with_reply(item):
            all_data: list = self.__data_reposity.data[self.__data_key]
            Creator_manager().remove_item(item)
            all_data.remove(item)

            return True
        else:
            return False


    def __get_filtered_data(self, _filter: dict):
        argument_exception.isinstance(_filter, dict)

        self.__filter_manager.update_filter_from_dict(_filter)
        all_data = self.__data_reposity.data[self.__data_key]

        data = self.__prototype.create(
            all_data,
            self.__filter_manager.filter,
            self.__filter_manager.filter_property,
            filtration_type.EQUALS
        ).data

        return data