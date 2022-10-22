#!/usr/bin/python3
"""  fetches https://alx-intranet.hbtn.io/status """

if __name__ == '__main__':
    from urllib.request import urlopen

    with urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print('Body reponse:')
        print(f'\t- type: {type(content)}')
        print(f'\t- content: {content}')
        print(f'\t- utf8 content: {content.decode("utf-8")}')
