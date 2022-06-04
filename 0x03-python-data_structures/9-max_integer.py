#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    for element in my_list:
        Max = my_list[0]
        if element > Max:
            Max = element
    return Max
