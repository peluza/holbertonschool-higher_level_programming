#!/usr/bin/python3
def safe_print_integer(value):
    value
    try:
        print("{:d}".format(value), end='\n')
        return True
    except:
        return False