#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_a_1 = 0
    if tuple_a == ():
        tuple_a_0 = 0
        tuple_a_1 = 0

    if len(tuple_b) == 1:
        tuple_b_1 = 0
    if tuple_b == ():
        tuple_b_0 = 0
        tuple_b_1 = 0

    tuple_a_0 = tuple_a[0]
    tuple_a_1 = tuple_a[1]

    tuple_b_0 = tuple_b[0]
    tuple_b_1 = tuple_b[0]

    tuple_sum0 = tuple_a_0 + tuple_b_0
    tuple_sum1 = tuple_a_1 + tuple_b_1

    tuple_sum = (tuple_sum0, tuple_sum1)
    return tuple_sum
