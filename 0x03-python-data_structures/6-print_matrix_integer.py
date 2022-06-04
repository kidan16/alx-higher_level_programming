#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for List in matrix:
        for element in List:
            if element == List[len(List) - 1]:
                print("{:d}".format(element))
                continue
            print("{:d}".format(element), end=" ")
