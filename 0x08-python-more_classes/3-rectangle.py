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
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            for row in range(self.__height):
                for column in range(self.__width):
                    rect.append("#")
                rect.append('\n')
        return "".join(rect)
