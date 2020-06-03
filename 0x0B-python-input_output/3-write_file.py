#!/usr/bin/python3
"""write_file
    """


def write_file(filename="", text=""):
    """write_file(filename, text)

    Keyword Arguments:
        filename {str} -- filename to create (default: {""})
        text {str} -- text add at file (default: {""})

    Returns:
        file -- the file with the text
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
