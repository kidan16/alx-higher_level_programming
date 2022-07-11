#!/usr/bin/python3
"""
A module to test the "Rectangle" class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    A class to test the Rectangle Class
    """

    def test_rectangle_subclass(self):
        """
        Test if Rectangle class inherit from
        Base class
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """
        Test parameters for Rectangle class
        """
        rectangle1 = Rectangle(10, 2)
        rectangle2 = Rectangle(2, 10)
        rectangle3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(rectangle1.id, 4)
        self.assertEqual(rectangle1.width, 10)
        self.assertEqual(rectangle1.height, 2)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)
        self.assertEqual(rectangle2.id, 5)
        self.assertEqual(rectangle2.width, 2)
        self.assertEqual(rectangle2.height, 10)
        self.assertEqual(rectangle2.x, 0)
        self.assertEqual(rectangle2.y, 0)
        self.assertEqual(rectangle3.id, 12)
        self.assertEqual(rectangle3.width, 10)
        self.assertEqual(rectangle3.height, 2)
        self.assertEqual(rectangle3.x, 0)
        self.assertEqual(rectangle3.y, 0)

        with self.assertRaises(TypeError):
            rectangle4 = Rectangle()

    def test_string(self):
        """
        Test string parameters for a
        Rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle('Monty', 'Python')

    def test_type_param(self):
        """
        Test different types of parameters
        for a Rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle(1.01, 3)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-234234242, 45)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle('', 4)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(True, 4)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 1.76)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, "Hello")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, -4798576398576)
            raise ValueError

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1.50)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 6, "test")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 7, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 7, -4798576398576)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1, 1.53)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 6, 5, "test")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 7, 7, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 9, 5, -4798576398576)
            raise ValueError()
