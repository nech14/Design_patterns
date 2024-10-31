from modules.Dto.filter_manager import Filter_manager
from modules.Dto.filtration_type import filtration_type
from modules.exceptions.argument_exception import argument_exception
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.process.modified_list import modified_list
from modules.process.processes.abstract_process import abstract_process
from modules.prototype.prototype import prototype


class create_warehouse_turnovers_date(abstract_process):

    @staticmethod
    def start_process(data: modified_list[warehouse_transaction_model]):
        from modules.process.list_processes import list_processes
        from modules.process.process_factory import Process_factory

        argument_exception.isinstance_list(data, modified_list, warehouse_transaction_model)

        process_factory = Process_factory()

        data_from_memory = process_factory.start_process(
            data=None,
            process=list_processes.read_result_turnovers.name
        )

        if data.block_period >= data.date:
            return data_from_memory

        filter_dict = {
            "period": [
                data.block_period,
                data.date
            ]
        }

        filter_manager = Filter_manager()
        filter_manager.update_filter_from_dict(filter_dict)

        prototype_obj = prototype()

        new_data = prototype_obj.create(
            data,
            filter_manager.filter,
            filter_manager.filter_property,
            filtration_type.INTERVAL
        ).date

        result = data_from_memory + new_data

        return result

