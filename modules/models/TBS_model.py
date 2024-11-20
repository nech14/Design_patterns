
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model


class TBS_model(abstract_model):

    __opening_remainder: list = None
    __remainder: list = None
    __incomes: list = None
    __expenses: list = None

    @property
    def opening_remainder(self):
        return self.__opening_remainder

    @opening_remainder.setter
    def opening_remainder(self, value: list):
        argument_exception.isinstance(value, list)

        self.__opening_remainder = value


    @property
    def incomes(self):
        return self.__incomes

    @incomes.setter
    def incomes(self, value: list):
        argument_exception.isinstance(value, list)

        self.__incomes = value


    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value: list):
        argument_exception.isinstance(value, list)

        self.__expenses = value

    @property
    def remainder(self):
        return self.__remainder

    @remainder.setter
    def remainder(self, value: list):
        argument_exception.isinstance(value, list)

        self.__remainder = value


    @staticmethod
    def create(
            name: str = "base_tbs",
            opening_remainder: list = None,
            incomes: list = None,
            expenses: list = None,
            remainder: list = None
    ):
        if opening_remainder is None:
            opening_remainder = []
        if incomes is None:
            incomes = []
        if expenses is None:
            expenses = []
        if remainder is None:
            remainder = []

        tbs = TBS_model()
        tbs.name = name
        tbs.opening_remainder = opening_remainder
        tbs.incomes = incomes
        tbs.expenses = expenses
        tbs.remainder = remainder

        return tbs

