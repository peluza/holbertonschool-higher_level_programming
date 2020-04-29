#!/usr/bin/python3
j = 1
for i in range(122, 96, -1):
    if j == -1:
        m = i - 32
    else:
        m = i
    print("{:c}".format(m), end='')
    j = j * (-1)
