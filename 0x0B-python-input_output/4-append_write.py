#!/usr/bin/python3
"""append_write
    """


def append_write(filename="", text=""):
    """append_write(filename, text)

    Keyword Arguments:
        filename {str} -- file name at modify (default: {""})
        text {str} -- text add at file (default: {""})

    Returns:
        file -- the file with the text,
                if the file exists add the text to the existing file
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
