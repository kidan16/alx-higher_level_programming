#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str)):
        return 0

    if roman_string is None:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    number = 0
    for _char in roman_string:
        number += roman[_char]
    value = []

    for char in roman_string:
        value.append(roman[char])

    j = 0
    for num in value[1:]:
        nump = value[j]
        if num > nump:
            number -= 2 * nump
        j += 1
    return number
