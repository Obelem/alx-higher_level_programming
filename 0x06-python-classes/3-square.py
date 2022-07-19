#!/usr/bin/python3
"""returns the current square area"""


class Square:
    """defines a square and raises both TypeError and ValueError if
    size is not int or < 0 respectively"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
