#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    Max = my_list[0]
    for element in my_list:
        if element > Max:
            Max = element
    return Max
