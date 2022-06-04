#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = 0
    if my_list == "":
        return None
    for l in range(0, len(my_list)):
        if my_list[l] > _max:
            _max = my_list[l]
    return _max
