#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request
    import sys
    from urllib.error import URLError, HTTPError

    
    try:
        url = sys.argv[1]
        data = parse.urlencode({"email": sys.argv[2]})
        data = data.encode()
        with request.urlopen(url, data) as response:
            print(response.read().decode('utf-8'))
    except URLError as e:
        print("Error code: ", e.code)
