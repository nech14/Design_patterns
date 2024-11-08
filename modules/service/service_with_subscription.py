
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.observers.abstract_observer import abstract_observer
from modules.service.abstract_service import abstract_service


class service_with_subscription(abstract_service):

    __observers = []

    def add_observer(self, o: abstract_observer):
        argument_exception.isinstance(o, abstract_observer)
        self.__observers.append(o)

    def remove_observer(self, o: abstract_observer):
        argument_exception.isinstance(o, abstract_observer)
        self.__observers.remove(o)

    def _notify(self, item: abstract_model):
        argument_exception.isinstance(item, abstract_model)
        for o in self.__observers:
            o.update(item)

    def _notify_with_reply(self, item:abstract_model):
        argument_exception.isinstance(item, abstract_model)
        reply = True

        for o in self.__observers:
            reply = reply and o.update(item)

        return reply
