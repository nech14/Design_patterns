from modules.exceptions.argument_exception import argument_exception
from modules.process.modified_list import modified_list
from modules.process.processes.abstract_process import abstract_process


class print_log_process(abstract_process):
    @staticmethod
    def start_process(data: modified_list):
        argument_exception.isinstance(data, modified_list)
        print(data.log_str)
