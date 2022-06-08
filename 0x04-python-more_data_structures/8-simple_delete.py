#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key_list = list(a_dictionary.keys())
    for key_word in key_list:
        if key_word == key:
            a_dictionary.pop(key)
    return a_dictionary
