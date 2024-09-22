
import re

from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.models.ingredient_model import ingredient_model
from modules.models.range_model import range_model


class receipt_model(abstract_model):

    __portions: int = 1
    __cooking_time: str = ""
    __steps:list[str] = []
    __ingredients:list[ingredient_model] = []


    @property
    def portions(self):
        return self.__portions

    @portions.setter
    def portions(self, value:int):
        argument_exception.isinstance(value, int)
        self.__portions = value


    @property
    def cooking_time(self):
        return self.__cooking_time

    @cooking_time.setter
    def cooking_time(self, value: str):
        argument_exception.isinstance(value, str)
        self.__cooking_time = value


    @property
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, value: list[str]):
        argument_exception.isinstance_list(value, list, str)
        self.__steps = value


    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value: list[ingredient_model]):
        argument_exception.isinstance_list(value, list, ingredient_model)
        self.__ingredients = value



    def set_compare_mode(self, other_object: 'receipt_model'):
        argument_exception().isinstance(other_object, receipt_model)
        return super().set_compare_mode(other_object=other_object)


