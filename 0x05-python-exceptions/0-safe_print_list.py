#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_num = 0
    for y in range(x):
        try:
            print('{:d}'.format(my_list[y]), end="")
            element_num += 1
        except IndexError:
            break
    print("")
    return element_num
