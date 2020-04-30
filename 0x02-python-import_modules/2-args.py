#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    a = len(argv) - 1
    j = 1
    if a == 0:
        print("{:d} arguments.".format(a))
    elif a == 1:
        print("{:d} argument:".format(a))
        for i in range(1, len(argv)):
            print("{:d}:".format(j), argv[i])
    else:
        print("{:d} arguments:".format(a))
        for i in range(1, len(argv)):
            print("{:d}:".format(j), argv[i])
            j += 1
