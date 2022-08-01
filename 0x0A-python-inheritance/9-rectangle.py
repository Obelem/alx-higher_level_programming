#!/usr/bin/python3
"""continuation of task 8:
    area() method gets implemented
    print() prints and str returns the rectangle description
"""
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
        """validates and initializes width and height of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """overrides string representation of Rectangle"""
        rect = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return rect
