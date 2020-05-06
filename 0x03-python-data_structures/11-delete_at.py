#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list == []:
        return None
    elif idx < 0:
        return my_list
    else:
        my_list.pop(idx)
    return my_list
