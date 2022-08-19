#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request
    import sys

    with request.urlopen(sys.argv[1]) as response:
        content = response.headers.get('X-Request-Id')
        print(content)
