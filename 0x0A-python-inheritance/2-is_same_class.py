#!/usr/bin/python3
"""checks if obj is exactly an instance of given class"""


def is_same_class(obj, a_class):
    """uses type to check for specific class"""
    return True if type(obj) is a_class else False
