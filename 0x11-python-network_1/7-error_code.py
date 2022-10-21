#!/usr/bin/python3
""" returns request content or error code with requests package """
from sys import argv
from requests import get

if __name__ == "__main__":
    req = get(argv[1])
    if req.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)
