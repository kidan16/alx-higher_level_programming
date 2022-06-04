#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_of_main_list in matrix:
        for element in list_of_main_list:
            print("{:d}".format(element), end=" ")
        print()
