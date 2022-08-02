#!/usr/bin/python3
"""writes a string to a text file(UTF8) and
    returns the number of chars written"""


def write_file(filename="", text=""):
    """uses open() and write() to write string to a text file.
    Return:
        no of characters read
    Args:
        filename: text file to write into
        text (str): string to write to text file
    """
    with open(filename, 'w', encoding='utf8') as file:
        return file.write(text)
