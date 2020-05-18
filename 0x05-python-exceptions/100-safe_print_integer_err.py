#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value), end='\n')
        return True
    except TypeError as ty:
        print("Exception:", ty, file=stderr)
        return False
    except ValueError as va:
        print("Exception:", va, file=stderr)
        return False
