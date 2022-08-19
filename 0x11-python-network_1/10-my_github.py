#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[1]
    token = sys.argv[2]
    Header = {'X-Github-Username': user,
              'X-Github-API-Token': token
              }
    res = requests.get("https://api.github.com/user", auth=(user, token))
    try:
        print(res.json()['id'])
    except Exception:
        print(None)
