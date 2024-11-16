
from modules.exceptions.argument_exception import argument_exception
from modules.observers.abstract_observer import abstract_observer


class observe_service:
    observers: list[abstract_observer] = []

    @staticmethod
    def append(observer: abstract_observer):
        if observer is None:
            return

        argument_exception.isinstance(observer, abstract_observer)

        items = list(map(lambda x: type(x).__name__, observe_service.observers))
        found = type(observer).__name__ in items
        if not found:
            observe_service.observers.append(observer)

    @staticmethod
    def raise_event(item):
        for instance in observe_service.observers:
            if instance is not None:
                instance.update(item)
