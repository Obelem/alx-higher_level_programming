#!/usr/bin/python3
"""raises an exception for non implementation of class"""


class BaseGeometry:
    """raises exception with message"""
    def area(self):
        raise Exception("area() is not implemented")
