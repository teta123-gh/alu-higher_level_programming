#!/usr/bin/python3
"""
Test Base class
"""
import unittest

from models.base import Base


class BaseTest(unittest.TestCase):
    """
    Test Base class
    """

    def test_auto_ids(self):
        """
        Test auto ids
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_manual_ids(self):
        """
        Test manual ids
        """
        b1 = Base(98)
        self.assertEqual(b1.id, 98)

    def test_ids_is_None(self):
        """
        Test ids is None
        """
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b1.id, b3.id - 2)

    def test_to_json_string_empty(self):
        """
        Test to_json_string empty
        """
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_none(self):
        """
        Test to_json_string None
        """
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_single_dict(self):
        """
        Test to_json_string single dict
        """
        dict_input = [{'id': 12}]
        json_output = Base.to_json_string(dict_input)
        self.assertEqual(json_output, '[{"id": 12}]')
        self.assertIsInstance(json_output, str)

    def test_from_json_string_empty(self):
        """
        Test from_json_string empty
        """
        list_output = Base.from_json_string("[]")
        self.assertEqual(list_output, [])
        self.assertIsInstance(list_output, list)

    def test_from_json_string_none(self):
        """
        Test from_json_string None
        """
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])
        self.assertIsInstance(list_output, list)

    def test_from_json_string_single_dict(self):
        """
        Test from_json_string single dict
        """
        list_output = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(list_output, [{'id': 89}])
        self.assertIsInstance(list_output, list)


if __name__ == '__main__':
    unittest.main()
