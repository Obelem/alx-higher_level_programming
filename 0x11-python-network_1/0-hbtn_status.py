#!/usr/bin/python3
# use urllib to fetch given url with formatted display

if __name__ == '__main__':
    from urllib.request import urlopen

    with urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
