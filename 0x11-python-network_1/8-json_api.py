#!/usr/bin/python3
""" first implementation of API's """

if __name__ == '__main__':
    from sys import argv
    from requests import post

    url = 'http://0.0.0.0:5000/search_user'
    letter = '' if len(argv) == 1 else argv[1]
    res = post(url, data={'q': letter})

    try:
        res_json = res.json()
        if res_json == {}:
            print('No result')
        else:
            print(f'[{res_json.get("id")}] {res_json.get("name")}')
    except Exception:
        print('Not a valid JSON')
