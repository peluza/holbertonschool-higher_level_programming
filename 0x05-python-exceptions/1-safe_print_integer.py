#!/usr/bin/python3
def safe_print_integer(value):
    value
    try:
        print("{:d}\n".format(value), end='')
        return True
    except:
        return False