#!/usr/bin/python3
"""
Contains the "Base" class
"""

import json


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == none or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string([]))

            list_dict = []

            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

            return f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = Rectangle(10, 16)
            id = dictionary["id"]
            width = dictionary["width"]
            height = dictionary["height"]
            x = dictionary["x"]
            y = dictionary["y"]

            obj = dummy.update(id=id, width=width, height=height, x=x, y=y)

        if cls.__name__ == 'Square':
            dummy = Square(10)
            id = dictionary["id"]
            size = dictionary["size"]
            x = dictionary["x"]
            y = dictionary["y"]

            obj = dummy.update(id=id, width=size, x=x, y=y)

        return obj.__str__()
