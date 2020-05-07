#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    new = sorted(a_dictionary.items(), key=lambda xy: (xy))
    x, y = new[-1]
    return x

