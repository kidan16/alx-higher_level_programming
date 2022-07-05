#!/usr/bin/python3
"""
Module 2-append_write
"""


def append_write(filename="", text=""):
    """ appends a text to a given file """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
