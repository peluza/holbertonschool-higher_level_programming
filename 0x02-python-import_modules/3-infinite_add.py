#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    a = len(argv) - 1
    result = 0
    if a == 0:
        print(result)
    elif a > 0:
        for i in range(1, len(argv)):
            result = result + int(argv[i])
        print(result)
