#!/usr/bin/python3
"""the body of the response."""


import requests
import sys


if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'
    data = requests.auth.HTTPBasicAuth(user, passwd)
    try:
        req = requests.get(url, auth=data)
        json = req.json()
        print(json['id'])
    except:
        print("None")
