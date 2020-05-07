#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    tmp = None
    for i, j in a_dictionary.items():
        if not tmp or j > a_dictionary[tmp]:
            tmp = i
    return tmp
