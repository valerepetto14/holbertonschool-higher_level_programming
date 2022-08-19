#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[1]
    token = sys.argv[2]
    Header = {'X-Github-Username': user,
              'X-Github-API-Token': token
              }
    res = requests.get("https://api.github.com/user", auth=(user, token))
    if len(res.json()['id']) != 0:
        print(res.json()['id'])
    else:
        print('None')
