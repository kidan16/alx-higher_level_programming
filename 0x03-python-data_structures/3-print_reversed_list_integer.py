#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        return
    my_list.reverse()
    for List in my_list:
        print("{:d}".format(List))
