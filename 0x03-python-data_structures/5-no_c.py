#!/usr/bin/python3
def no_c(my_string):
    new_list = ""
    for l in my_string:
        if l == "c" or l == 'C':
            continue
        new_list = new_list + l
    return new_list
