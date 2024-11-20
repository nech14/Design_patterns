from modules.Enums.event_type import event_type
from modules.exceptions.abstract_logic import abstract_logic
from modules.exceptions.argument_exception import argument_exception
from modules.observers.abstract_observer import abstract_observer


class observe_service:
    observers: list[abstract_logic] = []

    @staticmethod
    def append(observer: abstract_logic):
        if observer is None:
            return

        argument_exception.isinstance(observer, abstract_logic)

        items = list(map(lambda x: type(x).__name__, observe_service.observers))
        found = type(observer).__name__ in items
        if not found:
            observe_service.observers.append(observer)

    @staticmethod
    def raise_event(event: event_type, **kwargs):
        for instance in observe_service.observers:
            if instance is not None:
                instance.raise_event(event, **kwargs)
