#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    for j in range(x):
        try:
            print('{:d}'.format(my_list[j]), end="")
            z += 1
        except (IndexError, ValueError, TypeError):
            return
    print("")
    return z
