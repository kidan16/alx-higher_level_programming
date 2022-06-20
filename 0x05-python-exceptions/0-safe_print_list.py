#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for y in range(x):
        try:
            print('{:d}'.format(my_list[y]), end="")
        except (IndexError, TypeError, ValueError):
            return
    print("")
    return (y + 1)
