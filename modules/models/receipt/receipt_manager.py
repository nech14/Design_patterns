import re
from copy import copy

from modules.exceptions.abstract_logic import abstract_logic
from modules.models.nomenclature_model import nomenclature_model
from modules.models.receipt.receipt_model import receipt_model
from modules.exceptions.argument_exception import argument_exception
from modules.models.ingredient_model import ingredient_model
from modules.models.range_model import range_model


class receipt_manager(abstract_logic):
    __receipt: receipt_model = None
    __nomenclatures:list[nomenclature_model] = []
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, nomenclatures:list[nomenclature_model]=None):
        if nomenclature_model is None:
            pass
        else:
            argument_exception.isinstance_list(nomenclatures, list, nomenclature_model)
            self.__nomenclatures = nomenclatures

        if self.__receipt is None:
            self.__receipt = receipt_model()


    @property
    def receipt(self):
        return self.__receipt

    @receipt.setter
    def receipt(self, value: receipt_model):
        argument_exception.isinstance(value, receipt_model)
        self.__receipt = value


    def read_file(self, file_path:str, encoding='utf-8'):
        argument_exception.isinstance(file_path, str)
        argument_exception.isinstance(encoding, str)
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
        range_buf = []
        for name, grams in zip(ingredients_names, grams):
            i_m = ingredient_model()
            i_m.name = name
            buf = re.match(r"(\d+)\s*(\D+)", grams)
            i_m.value = int(buf.group(1))

            range_instance = range_model(buf.group(2).strip(), 1)

            if range_instance in range_buf:
                i_m.range = range_buf[range_buf.index(range_instance)]
            else:
                range_buf.append(range_instance)
                i_m.range = range_instance

            i_m.nomenclature = nomenclature_model.found_by_name(self.__nomenclatures, name)

            ingredients.append(i_m)

        self.receipt.name = title
        self.receipt.portions = int(portions)
        self.receipt.cooking_time = cook_time
        self.receipt.ingredients = ingredients
        self.receipt.steps = steps


    def save_in_file(self, file_path):
        # Формируем содержимое файла
        md_content = f"# {self.receipt.name}\n\n"
        if self.receipt.portions == 1:
            md_content += f"#### `{self.receipt.portions} порция`\n\n"
        else:
            md_content += f"#### `{self.receipt.portions} порций`\n\n"

        # Добавляем раздел с ингредиентами
        md_content += "| Ингредиенты     | Граммовка |\n"
        md_content += "|-----------------|-----------|\n"

        for i in self.receipt.ingredients:
            md_content += f"| {i.name} | {i.value} {i.range.name} |\n"

        # Добавляем раздел с шагами приготовления
        md_content += "\n## ПОШАГОВОЕ ПРИГОТОВЛЕНИЕ\n"
        md_content += f"Время приготовления: `{self.receipt.cooking_time}`\n\n"
        for i, step in enumerate(self.receipt.steps, 1):
            md_content += f"{i}. {step}\n\n"

        # Записываем содержимое в файл
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(md_content)

    """
    Перегрузка абстрактного метода
    """

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)


