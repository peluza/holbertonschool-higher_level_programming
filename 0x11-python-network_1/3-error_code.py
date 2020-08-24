#!/usr/bin/python3
"""body of the response"""

import urllib.request
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except urllib.error.HTTPError as error:
        type_error = error.code
        print("Error code: {}".format(type_error))
