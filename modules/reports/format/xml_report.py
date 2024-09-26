
import xml.etree.ElementTree as ET
from xml.dom import minidom

from modules.data_reposity import data_reposity
from modules.exceptions.argument_exception import argument_exception
from modules.models.abstract_model import abstract_model
from modules.reports.abstract_report import abstract_report
from modules.reports.format_reporting import format_reporting
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service


class xml_report(abstract_report):

    def __init__(self) -> None:
       super().__init__()
       self.__format = format_reporting.XML

    # Рекурсивная функция для создания XML элементов из словаря
    def __dict_to_xml(self, tag, data):
        element = ET.Element(tag)
        if isinstance(data, dict):
            for key, val in data.items():
                child = ET.SubElement(element, key)
                if isinstance(val, (dict, list)):
                    child.append(self.__dict_to_xml(key, val))
                else:
                    child.text = str(val)
        elif hasattr(data, 'get_dict'):
            # Если объект имеет метод get_dict(), используем его
            dict_representation = data.get_dict()
            for key, val in dict_representation.items():
                child = ET.SubElement(element, key)
                if isinstance(val, (dict, list)):
                    child.append(self.__dict_to_xml(key, val))
                else:
                    child.text = str(val)
        elif isinstance(data, list):
            for item in data:
                child = self.__dict_to_xml('item', item)
                element.append(child)
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





d_r = data_reposity()
m_s = Settings_manager()

s_s = start_service(d_r, m_s)
s_s.create()

rep = xml_report()
keys = list(s_s.reposity.data.keys())
print(keys)
rep.create(s_s.reposity.data[keys[3]])
print(rep.result)
print('\n')
