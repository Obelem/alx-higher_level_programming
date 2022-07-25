#!/usr/bin/python3

class Rectangle:
    """define a class 'Rectangle'"""
    def __init__(self, width=0, height=0):
        """initialize the class
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.__height = height
        self.__width = width

    @property
    """get current size of width"""
    def width(self):
        return self.__height

    @property
    "get current size of height"""
    def height(self):
        return self.__height

    @width.setter
    """set width size"""
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    "set height size"""
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
