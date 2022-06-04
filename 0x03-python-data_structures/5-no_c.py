#!/usr/bin/python3
def no_c(my_string):
    new_list = ""
    for Char in my_string:
        if Char == "c" or Char == 'C':
            continue
        new_list = new_list + Char
    return new_list
