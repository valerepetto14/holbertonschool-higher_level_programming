#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments
in order to solve this challenge.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    user = argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, user)
    res = requests.get(url)
    data = res.json()
    cont = 0
    for i in data:
        if cont < 10:
            print("{}: {}".format(i.get('sha'), i.get('commit')
                                  .get('author').get('name')))
        cont = cont + 1
