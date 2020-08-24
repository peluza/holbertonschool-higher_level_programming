#!/usr/bin/python3
"""Errors http"""


import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    html = requests.get(url)
    if html.status_code < 400:
        print(html.text)
    else:
        print("Error code: {}".format(html.status_code))
