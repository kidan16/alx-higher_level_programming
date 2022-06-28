#!/usr/bin/python3
"""
LockedClass
"""


class LockedClass:
    """ No class or object attributes, can't set
        Except for first_name
    """
    def __setattr__(self, attribute, value):
        word = "'LockedClass' object has no attribute '"
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError(word + attribute + "'")
