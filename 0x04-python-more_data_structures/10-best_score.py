#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {}:
        return None

    key_list = list(a_dictionary.keys())
    if len(key_list) == 0:
        return None

    _max = 0
    for key_word in key_list:
         if a_dictionary[key_word] > _max:
             _max = a_dictionary[key_word]
    for key_word in key_list:
        if a_dictionary[key_word] == _max:
            return a_dictionary[key_word]
