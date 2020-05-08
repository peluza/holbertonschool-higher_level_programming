#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for a, b in list(a_dictionary.items()):
        if b == value:
            del a_dictionary[a]
    return a_dictionary
