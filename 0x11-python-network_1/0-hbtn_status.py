#!/usr/bin/python3
"""  fetches https://alx-intranet.hbtn.io/status """

if __name__ == '__main__':
    from urllib.request import urlopen
    from urllib.request import Request

    req = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(req) as res:
        content = res.read()
        print('Body reponse:')
        print('\t- type:', type(content))
        print('\t- content:', content)
        print('\t- utf8 content:', content.decode('utf-8'))
