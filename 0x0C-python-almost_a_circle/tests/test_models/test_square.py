#!/usr/bin/python3
"""
A module to test the "Square" class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    A class to test the Square Class
    """

    def test_getter(self):
        self.assertEqual(Square(100).size, 100)

    def test_setter(self):
        square = Square(1)
        square.size = 100
        self.assertEqual(r1.size, 100)

    def test_string(self):
        square = Square(100)

        with self.assertRaises(TypeError):
            square.size = "Hello"

    def test_negative(self):
        square = Square(100)

        with self.assertRaises(ValueError):
            square.size = -100

    def test_zero(self):
        square = Square(100)

        with self.assertRaises(ValueError):
            square.size = 0

    def test_decimal(self):
        square = Square(100)

        with self.assertRaises(TypeError):
            square.size = 1.5

    def test_tuple(self):
        square = Square(100)

        with self.assertRaises(TypeError):
            square.size = (100, 200)

    def test_empty(self):
        square = Square(100)

        with self.assertRaises(TypeError):
            square.size = ""

    def test_none(self):
        square = Square(100)

        with self.assertRaises(TypeError):
            square.size = None

    def test_list(self):
        square = Square(100)

        with self.assertRaises(TypeError):
            square.size = [100, 200]

    def test_dict(self):
        square = Square(100)

        with self.assertRaises(TypeError):
            r1.size = {"Hello": 100, "world": 200}

    def test_width(self):
        square = Square(100)
        square.size = 200
        self.assertEqual(square.width, 100)
        self.assertEqual(square.height, 100)

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0

        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected)

        s1 = Square(1, 0, 0, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 0, 'size': 1, 'y': 0}
        self.assertEqual(s1_dictionary, expected)

        s1.update(5, 5, 5, 5)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 5, 'x': 5, 'size': 5, 'y': 5}
        self.assertEqual(s1_dictionary, expected)
