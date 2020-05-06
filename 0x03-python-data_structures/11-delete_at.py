#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list == []:
        return None
    i len(my_list) -1
    elif idx < 0 and idx > i:
        return my_list
    else:
        my_list.pop(idx)
        return my_list
