#!/usr/bin/python3
""" Interview task """

if __name__ == "__main__":
    from sys import argv
    from requests import get

    url = f'https://api.github.com/repos/{argv2}/{argv1}/commits'

    res = get(url)
    commits = res.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
