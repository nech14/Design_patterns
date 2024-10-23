
from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.models.nomenclature_model import nomenclature_model
from modules.models.range_model import range_model
from modules.models.warehouse_model import warehouse_model
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.models.warehouse_turnover_model import warehouse_turnover_model


class Process_factory(abstract_logic):

    __data = []
    __warehouse_turnovers = []


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value: list[warehouse_transaction_model]):
        argument_exception.isinstance_list(value, list, warehouse_transaction_model)

        self.__data = value

    @property
    def warehouse_turnovers(self):
        return self.__warehouse_turnovers



    def __create_item_dict(self, warehouse: warehouse_model):
        argument_exception.isinstance(warehouse, warehouse_model)

        item = {}
        item["warehouse"] = warehouse
        item["nomenclature"] = list()
        item["range"] = list()
        item["turnover"] = list()

        return item


    def __update_item_dict(self, item_dict, warehouse_transaction:warehouse_transaction_model):
        argument_exception.isinstance(warehouse_transaction, warehouse_transaction_model)

        nomenclature_list: list = item_dict["nomenclature"]
        range_list: list = item_dict["range"]
        turnover_list: list = item_dict["turnover"]

        exists = False
        turnover = None
        #check for existence
        if warehouse_transaction.nomenclature in nomenclature_list:
            index = nomenclature_list.index(warehouse_transaction.nomenclature)
            if warehouse_transaction.range == range_list[index]:
                turnover = turnover_list[index]
                exists= True

        if not exists:
            nomenclature_list.append(warehouse_transaction.nomenclature)
            item_dict["nomenclature"] = nomenclature_list

            range_list.append(warehouse_transaction.range)
            item_dict["range"] = range_list

            turnover = 0
            transaction_operation = warehouse_transaction_model.operation_transaction(
                warehouse_transaction.transaction_type.value
            )
            new_turnover = transaction_operation(turnover, warehouse_transaction.quantity)
            turnover_list.append(new_turnover)

        else:
            transaction_operation = warehouse_transaction_model.operation_transaction(warehouse_transaction.transaction_type.value)
            new_turnover = transaction_operation(turnover, warehouse_transaction.quantity)
            turnover_list[index]=new_turnover

        item_dict["turnover"] = turnover_list

        return item_dict


    def __create_warehouse_turnover(
            self,
            warehouse:warehouse_model,
            nomenclature:nomenclature_model, range:range_model, turnover:int=0):

        item_warehouse_turnover = warehouse_turnover_model()
        item_warehouse_turnover.warehouse = warehouse
        item_warehouse_turnover.nomenclature = nomenclature
        item_warehouse_turnover.range = range
        item_warehouse_turnover.turnover = turnover

        return item_warehouse_turnover


    def create_warehouse_turnovers(self, data: list[warehouse_transaction_model]=None):
        if data is None:
            data = self.__data
        argument_exception.isinstance_list(data, list, warehouse_transaction_model)

        pre_result = {}

        for i  in data :
            i: warehouse_transaction_model

            if not i.warehouse.unique_code in pre_result.keys():
                item_dict = self.__create_item_dict(i.warehouse)
            else:
                item_dict = pre_result[i.warehouse.unique_code]

            item_dict = self.__update_item_dict(item_dict, i)

            pre_result[i.warehouse.unique_code] = item_dict


        result = []
        for k, v in pre_result.items():
            v: dict
            item_warehouse = v['warehouse']

            nomenclature_list: list = v["nomenclature"]
            range_list: list = v["range"]
            turnover_list: list = v["turnover"]

            for i in range(len(nomenclature_list)):
                i:int
                item_warehouse_turnover = self.__create_warehouse_turnover(
                    item_warehouse,
                    nomenclature_list[i],
                    range_list[i],
                    turnover_list[i]
                )

                result.append(item_warehouse_turnover)


        self.__warehouse_turnovers = result
        return result

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
