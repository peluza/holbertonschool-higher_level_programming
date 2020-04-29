#!/usr/bin/python3
def uppercase(str):
    str = str + "\n"
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            lett_num = ord(str[i]) - 32
        else:
            lett_num = ord(str[i])
        print("{:c}".format(lett_num), end='')
