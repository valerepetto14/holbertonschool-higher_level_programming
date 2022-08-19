#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode("utf-8"))
