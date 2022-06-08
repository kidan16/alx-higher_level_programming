#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_word = list(a_dictionary.keys())
    key_word.sort()
    for element in key_word:
        print("{:s}: {}".format(element, a_dictionary[element]))
