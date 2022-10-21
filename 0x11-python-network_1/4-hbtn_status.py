#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
from requests import get

if __name__ == '__main__':
    res = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(res.text))
    print('\t- content:', res.text)
