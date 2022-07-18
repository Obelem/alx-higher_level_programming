#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Exception: unkwown format code 'd'\
 for object of type 'str'", file=sys.stderr)
        return False
