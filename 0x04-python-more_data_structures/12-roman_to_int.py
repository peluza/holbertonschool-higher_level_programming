#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for a, b in zip(roman_string, roman_string[1:]):
        if roman[a] < roman[b]:
            num -= roman[a]
        else:
            num += roman[a]
    num += roman[roman_string[-1]]
    return num
