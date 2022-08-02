#!/usr/bin/python3
"""creates python object from json file"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename (file pointer): json file to load
    """
    with open(filename) as file:
        return json.loads(file.read())
