#!/usr/bin/python3
"""  fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    from urllib.request import urlopen, Request

    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as res:
        content = res.read()

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
