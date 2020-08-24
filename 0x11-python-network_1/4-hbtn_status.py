#!/usr/bin/python3
""" that fetches"""


import requests


if __name__ == "__main__":

    html = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("	- type: {}".format(type(html.text)))
    print("	- content: {}".format(html.text))
