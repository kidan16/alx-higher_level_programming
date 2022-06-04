#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for l in range(0, len(my_list)):
        print("{:d}".format(my_list[len(my_list) - 1 - l]))
