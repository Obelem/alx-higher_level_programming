#!/usr/bin/python3
"""first go at inheritance"""


class MyList(list):
    """access methods of list class"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
