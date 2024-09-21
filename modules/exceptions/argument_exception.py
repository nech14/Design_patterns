from modules.exceptions.base_exception import base_exeption


class argument_exception(base_exeption):
    def __init__(self, message: str = "Invalid type!", argument_name:str = ""):
        self.argument_name = argument_name
        self.message = f"{message}: {argument_name}"
        super().__init__(self.message)

    @staticmethod
    def isinstance(_object, _type):
        if not isinstance(_object, _type):
            raise argument_exception(argument_name=f"{_object.__class__.__name__} != {_type.__name__}")


    @staticmethod
    def isinstance_list(_object, type_object, type_item):
        if not isinstance(_object, type_object) or not all(isinstance(item, type_item) for item in _object):
            raise argument_exception(argument_name=f"{_object.__class__.__name__}[{_object[0].__class__.__name__}] != {type_object.__name__}[{type_item.__name__}]")
