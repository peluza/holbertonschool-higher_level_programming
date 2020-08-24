#!/usr/bin/python3
"""the body of the response."""


import requests
import sys


if __name__ == "__main__":

    user = sys.argv[2]
    rep = sys.argv[1]
    url = "https://api.github.com/repos/" + user + "/" + rep + "/commits"
    try:
        req = requests.get(url)
        json = req.json()
        for i in json:
            print("{}: {}".format(i['sha'], i['commit']['author']['name']))
    except:
        print("None")
