#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = 0
    if my_list == "":
        return None
    for element in my_list:
        if element > _max:
            _max = element
    return _max
