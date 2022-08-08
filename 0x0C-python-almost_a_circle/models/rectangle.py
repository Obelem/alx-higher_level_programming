#!/usr/bin/python3
"""Inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """defines a rectangle with properties inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """define dimensions of Rectangle
        Args:
            width (int): Rectangle width
            height (int): Rectangle height
            x:
            y:
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x co-ordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x-coordinate"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y-coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y-coordinate"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the # character"""
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x, end="")
            for col in range(self.width):
                print("#", end="\n" if col == self.width - 1 else "")

    def __str__(self):
        """return custom string representation of object"""
        str1 = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
        str2 = f"{self.width}/{self.height}"
        return str1 + str2

    def update(self, *args, **kwargs):
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dict representation of Rectangle"""
        attr = ["x", "y", "id", 'height', 'width']
        rect_dict = {}

        for key in attr:
            rect_dict[key] = getattr(self, key)

        return rect_dict
