#!/usr/bin/python3
"""the body of the response."""


import requests
import sys


if __name__ == "__main__":

    rep = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/" + user + "/" + rep + "/commits"
    try:
        req = requests.get(url)
        json = req.json()
        count = 0
        for i in json:
            print("{}: {}".format(i['sha'], i['commit']['author']['name']))
            count += 1
            if count == 10:
                break
    except:
        print("None")
