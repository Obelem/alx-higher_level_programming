#!/usr/bin/python3
"""writes an object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args
        my_obj (dict): object to be converted to a JSON object
        filename (file pointer): pointer to json file
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
