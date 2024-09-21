
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


    def read_file(self, file_path:str, encoding='utf-8'):
        argument_exception.isinstance(file_path, str)
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()
        # Название рецепта
        title = re.search(r"# (.+)", content).group(1)

        # Количество порций
        portions_match = re.search(r"(\d+)\s*порц", content)
        portions = portions_match.group(1) if portions_match else "Unknown"

        # Ингредиенты и граммовка
        ingredients_section = re.findall(r"\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|", content)
        ingredients_names = [item[0].strip() for item in ingredients_section[2:]]  # Убираем заголовок
        grams = [item[1].strip() for item in ingredients_section[2:]]  # Убираем заголовок

        # Время приготовления
        cook_time = re.search(r"Время приготовления: `(.+?)`", content).group(1)

        # Шаги приготовления
        steps_section = re.split(r"\n\d+\.\s", content)[1:]  # Разделяем по шагам (начинаются с "1. ...")
        steps = [step.strip() for step in steps_section]

        ingredients = []
        for name, grams in zip(ingredients_names, grams):
            i_m = ingredient_model()
            i_m.name = name
            buf = re.match(r"(\d+)\s*(\D+)", grams)
            i_m.grams = int(buf.group(1))
            i_m.range = range_model(buf.group(2).strip(), 1)

            ingredients.append(i_m)

        self.name = title
        self.portions = int(portions)
        self.cooking_time = cook_time
        self.ingredients = ingredients
        self.steps = steps


    def save_in_file(self, file_path):
        # Формируем содержимое файла
        md_content = f"# {self.name}\n\n"
        if self.portions == 1:
            md_content += f"#### `{self.portions} порция`\n\n"
        else:
            md_content += f"#### `{self.portions} порций`\n\n"

        # Добавляем раздел с ингредиентами
        md_content += "| Ингредиенты     | Граммовка |\n"
        md_content += "|-----------------|-----------|\n"

        for i in self.ingredients:
            md_content += f"| {i.name} | {i.grams} {i.range.name} |\n"

        # Добавляем раздел с шагами приготовления
        md_content += "\n## ПОШАГОВОЕ ПРИГОТОВЛЕНИЕ\n"
        md_content += f"Время приготовления: `{self.cooking_time}`\n\n"
        for i, step in enumerate(self.steps, 1):
            md_content += f"{i}. {step}\n\n"

        # Записываем содержимое в файл
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(md_content)


    def set_compare_mode(self, other_object: 'receipt_model'):
        argument_exception().isinstance(other_object, receipt_model)
        return super().set_compare_mode(other_object=other_object)


