#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 2:
        datos = sys.argv[1]
    else:
        datos = ""
    res = requests.post("http://0.0.0.0:5000/search_user", {q: datos})
    try:
        data = res.json()
        if len(data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except Exception:
        print("Not a valid JSON")
