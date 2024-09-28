from modules.exceptions.argument_exception import argument_exception


class length_exception(argument_exception):
    def __init__(self, max_len:int, argument_name:str=None):
        self.message = f"Length {argument_name} exceeds maximum length by {max_len}"
        super().__init__(message=self.message, argument_name=argument_name)

    @staticmethod
    def length_zero():
        super().__init__(message="The argument is empty", argument_name="")

