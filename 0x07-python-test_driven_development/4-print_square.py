#!/usr/bin/python3
"""prints a square"""


def print_square(size):
    """prints a square with char '#'
    Args:
        size (int): size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end='\n' if col == size - 1 else "") 
