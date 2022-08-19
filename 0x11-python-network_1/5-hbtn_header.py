#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.get(sys.argv[1])
    print(res.headers['X-Request-Id'])
    