#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary_copy = a_dictionary.copy()
    x = 1
    key_list = list(a_dictionary_copy.keys())
    for key_word in key_list:
        if key_word == key:
            a_dictionary_copy[key] = value
        else:
            x = 0
    if x == 0:
        a_dictionary_copy[key] = value

    return a_dictionary_copy
