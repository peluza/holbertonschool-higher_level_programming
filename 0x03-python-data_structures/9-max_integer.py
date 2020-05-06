#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list)
    tmp = my_list[0]
    if i == 0:
        return None
    else:
        for i in my_list:
            if i > tmp:
                tmp = i
        return (tmp)
