#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, attribute, value):

        word = "'LockedClass' object has no attribute '"

        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError(word + attribute + "'")
