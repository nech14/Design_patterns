import unittest

from modules.Dto.filter_manager import Filter_manager
from modules.Dto.filter_objects import filter_objects
from modules.models.range_model import range_model


class MyTestCase(unittest.TestCase):

    filter_manager = Filter_manager()

    def test_update_filters(self):
        self.filter_manager.filter_object = filter_objects.base_filter
        self.filter_manager.update_filter_property()

        self.assertEqual(
            self.filter_manager.filter_property,
            ['model_unique_code', 'name']
        )

        self.filter_manager.update_filter()
        filter = self.filter_manager.filter
        for attr in self.filter_manager.filter_property:
            self.assertEqual(
                getattr(filter, attr),
                ""
            )

        dict_for_filter = {
            "model_unique_code": "0",
            'name': 'Пшеничная мука',
            "test_list": list["1", "2"],
            "test_range": range_model("гр", 1)
        }

        self.filter_manager.update_filter_from_dict(dict_for_filter)
        filter = self.filter_manager.filter

        for attr, value in dict_for_filter.items():
            self.assertEqual(
                getattr(filter, attr),
                value
            )


