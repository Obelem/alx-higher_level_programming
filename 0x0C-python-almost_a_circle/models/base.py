#!/usr/bin/python3
"""Creates the first class -> Base"""


class Base:
    """defines the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
