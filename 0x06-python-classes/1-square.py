#!/usr/bin/python3
"""Defines a square by Private instance attribute: size"""


class Square:
    """instantiate class with size(no type/value verification)"""
    def __init__(self, size):
        self.__size = size
