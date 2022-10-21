#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""

if __name__ == '__main__':
    from urllib.request import urlopen

    with urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print('Body reponse:')
        print('\t- type:', type(content))
        print('\t- content:', content)
        print('\t- utf8 content:', content.decode('utf-8'))
