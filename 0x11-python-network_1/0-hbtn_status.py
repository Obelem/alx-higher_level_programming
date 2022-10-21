#!/usr/bin/python3
"""use urllib to fetch given url with formatted display"""
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print('Body reponse:')
        print('\t- type:', type(content))
        print('\t- content:', content)
        print('\t- utf8 content:', content.decode('utf-8'))
