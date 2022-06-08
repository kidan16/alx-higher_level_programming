#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) != dict or a_dictionary == {}:
        return None
    key_list = list(a_dictionary.keys())
    _max = 0
    for key_word in key_list:
         if a_dictionary[key_word] > _max:
             _max = a_dictionary[key_word]
    for key_word in key_list:
        if a_dictionary[key_word] == _max:
            return a_dictionary[key_word]
