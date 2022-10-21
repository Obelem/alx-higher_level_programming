#!/usr/bin/python3
# use urllib to fetch given url with formatted display

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print('Body reponse:')
        print('\t- type:', type(content))
        print('\t- content:', content)
        print('\t- utf8 content:', content.decode('utf-8'))
