#!/usr/bin/python3
"""
MOdule 4-from_josn_string
"""

import json


def from_json_string(my_str):
    """ deserializes a json representation """
    return json.loads(my_str)
