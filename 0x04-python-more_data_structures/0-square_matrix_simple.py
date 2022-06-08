#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    array = [list(map(lambda x: x*x, _list)) for _list in matrix]
    return array
