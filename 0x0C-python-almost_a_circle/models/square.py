#!/usr/bin/python3
"""
Contains the "Square" class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=0, y=0, id=None)
        self.size = size

        @property
        def size(self):
            return self.width

        @size.setter
        def size(self, value):
            self.width = value
            self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        if args != none:
            for arg in args:
                if j == 0:
                    self.id = args[0]
                if j == 1:
                    self.id = args[1]
                if j == 2:
                    self.x = args[2]
                if j == 3:
                    self.y = args[3]

        if kwargs != none:
            for key_word in kwargs.keys():
                if key_word == "id" and args == none:
                    self.id = kwargs["id"]
                if key_word == "size" and len(args) == 1:
                    self.size = kwargs["size"]
                if key_word == "x" and len(args) == 2:
                    self.x = kwargs["x"]
                if key_word == "y" and len(args) == 3:
                    self.y = kwargs["y"]

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
