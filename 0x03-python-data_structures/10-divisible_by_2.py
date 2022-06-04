#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for l in range(0, len(my_list)):
        if my_list[l] % 2 == 0:
            new_list[l] = True
        else:
            new_list[l] = False
    return new_list
