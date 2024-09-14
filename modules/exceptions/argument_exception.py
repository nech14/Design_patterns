from modules.exceptions.base_exception import base_exeption


class argument_exception(base_exeption):
    def __init__(self, message: str = "Invalid type!", argument_name:str = ""):
        self.argument_name = argument_name
        self.message = f"{message}: {argument_name}"
        super().__init__(self.message)
