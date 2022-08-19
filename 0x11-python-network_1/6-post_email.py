#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests
    import sys

    data = {"email": sys.argv[2]}
    res = requests.post(sys.argv[1], data)
    print("Your email is: ", res)
