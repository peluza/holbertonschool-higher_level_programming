#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)
    if i == 0:
        a = (0, None)
    else:
        a = (i, sentence[0])
    return a
