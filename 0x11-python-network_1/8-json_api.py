#!/usr/bin/python3
"""the body of the response."""


import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    req = requests.post(url, data)
    try:
        json = req.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))
    except ValueError:
        print("Not a valid JSON")
