#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request
    import sys
    from urllib.error import URLError, HTTPError

    try:
        url = sys.argv[1]
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except URLError as e:
        print("Error code: ", e.code)
