from modules.exceptions.argument_exception import argument_exception
from modules.models.TBS_model import TBS_model
from modules.models.abstract_model import abstract_model
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.models.warehouse_turnover_model import warehouse_turnover_model
from modules.process.modified_list import modified_list
from modules.Enums.transaction_type import enum_transaction_type


class create_TBS(abstract_model):

    @staticmethod
    def start_process(data: modified_list):
        if data is None:
            raise argument_exception(argument_name = f"data is None")

        argument_exception.isinstance(data, modified_list)

        if len(data) == 0:
            return []

        incomes = []
        expenses = []

        opening_remainder = {}
        remainder = {}

        for t in data.date:
            t : warehouse_transaction_model
            if t.period <= data.date:
                create_TBS.__adding_unique(opening_remainder, t)
            create_TBS.__adding_unique(remainder, t)


            if t.transaction_type == enum_transaction_type.Income:
                incomes.append(t)
            elif t.transaction_type == enum_transaction_type.Expense:
                expenses.append(t)


        opening_remainder = list(opening_remainder.values())
        remainder = list(remainder.values())

        tbs = TBS_model.create(
            opening_remainder=opening_remainder,
            remainder=remainder,
            incomes=incomes,
            expenses=expenses
        )

        return tbs


    @staticmethod
    def __adding_unique(_dict:dict, transaction: warehouse_transaction_model):
        argument_exception.isinstance(transaction, warehouse_transaction_model)
        argument_exception.isinstance(_dict, dict)

        check_data = (transaction.warehouse.unique_code, transaction.nomenclature.unique_code, transaction.range.unique_code)

        operation_transaction = warehouse_transaction_model.operation_transaction(transaction.transaction_type)

        if check_data in _dict.keys():
            turnover: warehouse_turnover_model = _dict[check_data]
        else:
            turnover = warehouse_turnover_model.create_default(
                warehouse=transaction.warehouse,
                nomenclature=transaction.nomenclature,
                range=transaction.range,
                turnover=0
            )

        quantity = operation_transaction(turnover.turnover, transaction.quantity)
        turnover.turnover = quantity

        _dict[check_data] = turnover

