#!/usr/bin/python3
"""the body of the response."""


import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    html = requests.post(url, values)
    print(html.text)
