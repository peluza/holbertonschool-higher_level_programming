#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list)
    tmp = my_list[0]
    if my_list == []:
        return None
    else:
        for i in my_list:
            if i > tmp:
                tmp = i
        return tmp
