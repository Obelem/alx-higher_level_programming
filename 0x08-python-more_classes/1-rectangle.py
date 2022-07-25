#!/usr/bin/python3
"""defines and initializes a class -> Rectangle"""


class Rectangle:
    """define a class Rectangle"""
    def __init__(self, width=0, height=0):
        """initialize the class
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """get current size of width"""
        return self.__height

    @width.setter
    def width(self, value):
        """set width size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get current size of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height size"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
