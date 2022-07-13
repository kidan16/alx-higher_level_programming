#!/usr/bin/python3
"""
Module: rectangle
Class: Rectangle
Inherited class: Base
"""

from models.base import Base


class Rectangle(Base):
    """A representation of a rectangle"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id=None)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints a Rectangle instance with the character # """
        for y_unit in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x, end="")
            for column in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Overrides the __str__ method"""
        str1 = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
        str2 = f"{self.width}/{self.height}"
        return str1 + str2

    def update(self, *args, **kwargs):
        """Updates the Rectangle"""
        if args != none:
            for j in range(len(args)):
                if j == 0:
                    self.id = args[0]
                if j == 1:
                    self.width = args[1]
                if j == 2:
                    self.height = args[2]
                if j == 3:
                    self.x = args[3]
                if j == 4:
                    self.y = args[4]

        if kwargs != none:
            for key_word in kwargs.keys():
                if key_word == "id" and args == none:
                    self.id = kwargs["id"]
                if key_word == "width" and len(args) == 1:
                    self.width = kwargs["width"]
                if key_word == "height" and len(args) == 2:
                    self.height = kwargs["height"]
                if key_word == "x" and len(args) == 3:
                    self.x = kwargs["x"]
                if key_word == "y" and len(args) == 4:
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        dict_x = {"x": self.x}
        dict_y = {"y": self.y}
        dict_id = {"id": self.id}
        dict_height = {"height": self.height}
        dict_width = {"width": self.width}
        return dict_x + dict_y + dict_id + dict_height + dict_width
