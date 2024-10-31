
from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.process.list_processes import list_processes


class Process_factory(abstract_logic):

    def __init__(self):
        super().__init__()
        pass


    def start_process(self, data: list, process: str):

        argument_exception.isinstance(data, list)
        argument_exception.isinstance(process, str)

        process_names = [member.name for member in list_processes]
        if not process in process_names:
            raise argument_exception(message=f"such a process({process}) is not implemented")

        result = list_processes[process].value.start_process(data)

        return result


    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
