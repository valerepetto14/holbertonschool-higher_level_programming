#!/usr/bin/python3
""" task 100 """

from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = get(url)
    for comit in r.json()[0:10]:
        print(comit.get('sha'), end=': ')
        print(comit.get('commit').get('author').get('name'))
