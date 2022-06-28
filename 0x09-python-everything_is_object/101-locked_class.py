#!/usr/bin/python3
"""
LockedClass
"""


class LockedClass:
    """ No class or object attributes, can't set
        Except for first_name
    """

    def __setattr__(self, attribute, value):
        if attribute is "first_name":
            self.__dict__[attribute] = {"first_name": value}
        else:
            word = "'LockedClass' object has no attribute '" + attribute + "'"
            raise AttributeError(word)
