from modules.exceptions.argument_exception import argument_exception
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.process.modified_list import modified_list
from modules.process.processes.abstract_process import abstract_process

class update_warehouse_turnovers_block_period(abstract_process):

    @staticmethod
    def start_process(data: modified_list[warehouse_transaction_model]):
        from modules.process.list_processes import list_processes
        from modules.process.process_factory import Process_factory

        argument_exception.isinstance_list(data, modified_list, warehouse_transaction_model)

        process_factory = Process_factory()

        result = process_factory.start_process(
            data,
            list_processes.create_warehouse_turnovers_date.name
        )

        result = modified_list(result)
        result.file_path = data.file_path

        status = process_factory.start_process(
            result,
            list_processes.save_result_turnover.name
        )

        return status



