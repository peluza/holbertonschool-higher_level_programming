#!/usr/bin/python3
"""the response header"""


import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    html = requests.get(url).headers.get('X-Request-Id')

    print(html)
