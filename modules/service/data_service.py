import json

from modules.Enums.event_type import event_type
from modules.creator_manager import Creator_manager
from modules.data_reposity import data_reposity
from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.service.observer_service import observe_service


class Data_service(abstract_logic):
    __trigger_events = [event_type.SAVE_DATA_REPOSITY, event_type.READ_DATA_REPOSITY]
    __file_path = "data_reposity.json"

    def __init__(self):
        super().__init__()
        observe_service.append(self)


    def raise_event(self, event: event_type, **kwargs):
        argument_exception.isinstance(event, event_type)

        if not event in self.__trigger_events:
            return

        data = kwargs.get('data')
        if data is None:
            raise argument_exception(message="data is None!")
        argument_exception.isinstance(data, data_reposity)

        def_fun = self.__events[self.__trigger_events.index(event)]

        def_fun(data)




    def __save_data(self, data:data_reposity):

        with open(self.__file_path, 'w') as f:
            json.dump(data.data, f, ensure_ascii=False, indent=1)

    def __read_data(self, data:data_reposity):

        with open(self.__file_path, 'r') as f:
            read_data = json.load(f)

        Creator_manager(read_data)
        data.data = Creator_manager().get_object()



    __events = [__save_data, __read_data]