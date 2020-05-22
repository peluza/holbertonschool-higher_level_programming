#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    if ". " in text:
        text = text.replace(". ", ".\n\n")
    if ": " in text:
        text = text.replace(": ", ":\n\n")
    if "? " in text:
        text = text.replace("? ", "?\n\n")
        print(text, end='')
