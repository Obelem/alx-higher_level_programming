#!/usr/bin/python3
"""returns dictionary representation of a class"""


class Student:
    """define Student class"""
    def __init__(self, first_name, last_name, age):
        """initialize public instance attributes
        Args:
            first_name (str): students first name
            last_name (str): students last name
            age (int): students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return __dict__ attribute"""
        return vars(self)
