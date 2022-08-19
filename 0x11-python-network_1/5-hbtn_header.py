#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests

    res = requests.get("https://intranet.hbtn.io/status")
    print(res.headers['X-Request-Id'])
    