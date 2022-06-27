#!/usr/bin/python3

"""Defines a rectangle class"""


class Rectangle:
    """Defines a Rectangle class with private attributes"""
    
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height
        Args:
            width : The width of the rectangle.
            height: The height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, widt):
        if type(widt) != int:
            raise TypeError("width must be an integer")
        if widt < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self, heigh):
        if type(heigh) != int:
            raise TypeError("height must be an integer")
        if heigh < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
