#!/usr/bin/python3
"""the body of the response."""


import requests
import sys


if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/repos/peluza/holbertonschool-higher_level_programming/commits'
    data = requests.auth.HTTPBasicAuth(user, passwd)
    try:
        req = requests.get(url, auth=data)
        json = req.json()
        for i in json:
            print("{}: {}".format(i['sha'], i['commit']['author']['name']))
    except:
        print("None")
