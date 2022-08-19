#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests
    import sys

    data = {'email': sys.argv[2]}
    try:
        res = requests.post(sys.argv[1], data)
        if (res.status_code >= 400):
            print("Error code: ", res.status_code)
        else:
            print(res.text)
