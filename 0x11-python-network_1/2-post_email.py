#!/usr/bin/python3
"""2-post_email.py"""
from sys import argv
from urllib import parse
from urllib.request import Request, urlopen

if __name__ == '__main__':
    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    request = Request(argv[1], data)
    with urlopen(request) as res:
        print(res.read().decode('utf-8'))
