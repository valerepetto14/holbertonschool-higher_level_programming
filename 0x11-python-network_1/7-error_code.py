#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.post(sys.argv[1])
    if (res.status_code >= 400):
        print("Error code: ", res.status_code)
    else:
        print(res.text)
