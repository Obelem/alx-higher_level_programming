#!/usr/bin/python3
"""returns JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Uses the dump() method of the json module to
    return the JSON representation of my_obj
    Args:
        my_obj (str): string to get JSON representation of
    """
    return json.dumps(my_obj)
