#!/usr/bin/python3
""" displays the value of the variable X-Request-Id in the response header """
from sys import argv
from requests import get

if __name__ == "__main__":
    print(get(argv[1]).headers.get('X-Request-Id'))
