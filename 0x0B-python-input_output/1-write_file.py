#!/usr/bin/python3
"""
Module 1-write_file
"""


def write_file(filename="", text=""):
    """ writes a text to a given file """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
