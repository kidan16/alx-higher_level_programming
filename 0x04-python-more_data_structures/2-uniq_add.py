#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = {x for x in my_list}
    _sum = 0
    for element in new_set:
        _sum += element
    return _sum
