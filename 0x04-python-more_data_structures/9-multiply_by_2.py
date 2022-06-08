#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary_copy = a_dictionary.copy()
    key_list = list(a_dictionary_copy.keys())
    for key in key_list:
        a_dictionary_copy[key] = 2 * a_dictionary_copy[key]
    return a_dictionary_copy
