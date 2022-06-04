#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for m in range(0, len(l)):
            print("{}".format(l[m]), end=" ")
        print()
