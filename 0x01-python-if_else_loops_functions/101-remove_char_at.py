#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        _list = []
        if (i == n):
            continue
        else:
            _list.append(str[i])
    string = ''.join([str(item) for item in _list])
    return string
