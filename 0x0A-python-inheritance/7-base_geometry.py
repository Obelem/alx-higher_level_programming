#!/usr/bin/python3
"""raises an exception for non implementation of class"""


class BaseGeometry:
    """raises exception with message"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value if it is
        i. an integer
        ii. <= 0
        and raises a TypeError and Value Error respectively
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
