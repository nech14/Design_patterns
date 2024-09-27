
import xml.etree.ElementTree as ET
from xml.dom import minidom

from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.reports.abstract_report import abstract_report
from modules.reports.format_reporting import format_reporting


class xml_report(abstract_report):

    def __init__(self) -> None:
       super().__init__()
       self.extension = "xml"
       self.__format = format_reporting.XML

    # Рекурсивная функция для создания XML элементов из словаря

    def __dict_to_xml(self, tag, data):
        element = ET.Element(tag)
        print(f"Creating XML for tag: {tag}, data: {data}")

        if isinstance(data, dict):
            for key, val in data.items():
                # Если значение - это словарь, создаем вложенный элемент
                if isinstance(val, dict):
                    child_item = ET.SubElement(element, key)
                    for child_key, child_val in val.items():
                        group_child = ET.SubElement(child_item, child_key)
                        group_child.text = str(child_val)
                # Если значение - это список, обрабатываем каждый элемент
                elif isinstance(val, list):
                    for item in val:
                        item_child = self.__dict_to_xml(key, item)
                        element.append(item_child)
                else:
                    child = ET.SubElement(element, key)
                    child.text = str(val)

        elif hasattr(data, 'get_dict'):
            dict_representation = data.get_dict()
            for key, val in dict_representation.items():
                if isinstance(val, dict):
                    child_item = ET.SubElement(element, key)
                    for child_key, child_val in val.items():
                        group_child = ET.SubElement(child_item, child_key)
                        group_child.text = str(child_val)
                elif isinstance(val, list):
                    for item in val:
                        item_child = self.__dict_to_xml(key, item)
                        element.append(item_child)
                else:
                    child = ET.SubElement(element, key)
                    child.text = str(val)

        else:
            element.text = str(data)

        return element


    # Преобразование списка словарей в XML
    def __list_of_dicts_to_xml(self, tag, data):
        root = ET.Element(tag)
        for item in data:
            item_element = self.__dict_to_xml('item', item)  # Создаем элемент для каждого словаря
            root.append(item_element)  # Добавляем элемент к корневому
        return root


    def create(self, data: list):
        argument_exception.isinstance_list(data, list, abstract_model)

        _xml = self.__list_of_dicts_to_xml(
            str(data[0].__class__.__name__),
            data
        )

        # Преобразование XML-элемента в строку
        xml_string = ET.tostring(_xml, encoding="unicode", method="xml")

        # Форматирование строки с помощью xml.dom.minidom
        formatted_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")

        # Удаление лишних новых строк
        self.result = "\n".join([line for line in formatted_xml.splitlines() if line.strip()])

