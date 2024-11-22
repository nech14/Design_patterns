from modules.Enums.event_type import event_type
from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.process.modified_list import modified_list
from modules.process.process_factory import Process_factory
from modules.settings.settings_manager import Settings_manager


class log_service(abstract_logic):

    __log_fun: list
    __setting_manager: Settings_manager
    __check_event_list: list = []

    def __new__(cls, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(log_service, cls).__new__(cls)
        return cls.instance


    def __init__(self, setting_manager: Settings_manager):
        argument_exception.isinstance(setting_manager, Settings_manager)
        self.__log_fun = [
            self.__debug,
            self.__info,
            self.__error
        ]
        self.__setting_manager = setting_manager

        self.__check_event_list = self.__log_fun[self.__setting_manager.settings.log_type.value]()


    def raise_event(self, event: event_type, **kwargs):
        print(event)
        print(self.__check_event_list)
        if event in self.__check_event_list:
            self.log(self.__setting_manager.settings.log_type, Event_type=event, **kwargs)


    def set_exception(self, ex: Exception):
        pass


    def __debug(self):
        return self.__info() + self.__error() + [

        ]

    def __info(self):
        return [
            event_type.SAVE_DATA_REPOSITY,
            event_type.READ_DATA_REPOSITY,
            event_type.WEB,
            event_type.INFO
        ]

    def __error(self):
        return [
            event_type.ERROR
        ]


    def log(self, event, **kwargs):
        body_log = ', '.join(f"{key}={value}" for key, value in kwargs.items())
        str_log = f"[{event.name}] {body_log}"
        data = modified_list()
        data.log_str = str_log
        data.file_path = self.__setting_manager.log_path
        Process_factory().start_process(data, self.__setting_manager.settings.log_process.name)
