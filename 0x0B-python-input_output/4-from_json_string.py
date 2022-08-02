#!/usr/bin/python3
"""returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """ Uses loads() from the json module to convert
    JSON string to python dictionary
    Args
        my_str (str): json string to convert
    """
    return json.loads(my_str)
