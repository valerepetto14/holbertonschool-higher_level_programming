#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request
    import sys
    from urllib.error import URLError, HTTPError

    url = sys.argv[1]
    try:
        request.urlopen(url)
    except HTTPError as e:
        print(e.reason)
