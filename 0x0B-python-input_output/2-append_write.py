#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8) and returns
    the number of chars added"""


def append_write(filename="", text=""):
    """
    Description: appends string at of text file
    Args:
        filename: file to append string to
        text (str): string to be appended
    Return:
        number of characters added
    """
    with open(filename, 'a', encoding='utf8') as file:
        return file.write(text)
