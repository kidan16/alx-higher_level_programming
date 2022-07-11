#!/usr/bin/python3
"""
A module to test the "Base" class
"""
import unittest
import json
from models import base
from models import rectangle
Base = base.Base
Rectangle = rectangle.Rectangle


class TestBase(unittest.TestCase):
    """
    A class to test the Base Class
    """

    def test_id_as_positive(self):
        """
        Test for a positive value of the keyword argument id
        """
        self.assertEqual(Base(16).id, 16)

    def test_id_as_negative(self):
        """
        Test for a negative value of the keyword argument id
        """
        self.assertEqual(Base(-16).id, -16)

    def test_id_as_none(self):
        """
        Test for a case id=None
        """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(id=None).id, 2)

    def test_id_as_string(self):
        """
        Test for a case id has a value of type str
        """
        self.assertEqual(Base("ID").id, "ID")

    def test_to_json_string(self):
        """
        Test the to_json_string method
        """
        list_dict = [Rectangle(16, 23, 1, 19, 100).to_dictionary()]
        json_string = "{'x': 1, 'width': 16, 'id': 100, 'height': 23, 'y': 19}"
        self.assertEqual(Base.to_json_string(list_dict, json_string))

    def test_empty_to_json_string(self):
        """
        Test to_json_string method without any argument or an empty list
        """

        self.assertEqual(Base.to_json_string(), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_instance(self):
        """
        Test a Base Class instance
        """
        self.assertEqual(type(Base()), Base)
        self.assertTrue(isinstance(Base(), Base), True)

    def test_wrong_to_json_string(self):
        """
        Test a wrong functionality of the
        to_json_string method
        """
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        warn = ("to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()

        self.assertEqual(warn, str(msg.exception))

        warn = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{1, 10}], [{16, 10}])

        self.assertEqual(warn, str(msg.exception))

    def test_wrong_save_to_file(self):
        """
        Test the save_to_file method
        """
        with self.assertRaises(AttributeError) as msg:
            Base.save_to_file([Base(1), Base(2)])

        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'",
             str(msg.exception)
        )

    def test_load_from_file(self):
        """
        Test the load_from_file method
        """
        if os.path.exists("Base.json"):
            os.remove("Base.json")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        rect_output = Rectangle.load_from_file()
        self.assertEqual(rect_output, [])

        square_output = Square.load_from_file()
        self.assertEqual(square_output, [])

        warn = "load_from_file() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Rectangle.load_from_file('Monty Python')

        self.assertEqual(warn, str(msg.exception))

    def test_create(self):
        """
        Test the create method
        """
        with self.assertRaises(TypeError) as msg:
            warn = Rectangle.create('Monty Python')

        self.assertEqual(
            "create() takes 1 positional argument but 2 were given",
            str(msg.exception)
        )
