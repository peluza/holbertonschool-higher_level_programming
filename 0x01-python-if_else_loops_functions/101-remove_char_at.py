#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if n >= 0:
            str1 = str[:n] + str[n + 1:]
        else:
            str1 = str
        return(str1)
