#!/usr/bin/python3
"""defines a function that reads a text file (UTF8) and prints to stdout"""


def read_file(filename=""):
    """ -Reads and prints text file in UTF8 encoding.
        -Makes use of the 'with' statement to simplify our
        write process
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
    file.close()
