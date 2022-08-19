#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request


import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.headers.get('X-Request-Id')
        print(content)