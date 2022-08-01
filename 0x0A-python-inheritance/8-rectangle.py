#!/usr/bin/python3
"""Inherits and validates an attribute"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    validates width and height values
    using integer_validator property inherited @ 7-base_geometry
    Args:
        width (int): rectangle width
        height (int): rectangle height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
