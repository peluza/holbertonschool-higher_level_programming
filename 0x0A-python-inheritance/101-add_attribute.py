#!/usr/bin/python3
"""101-add_attribute
    """


def add_attribute(self, name, atribute):
    """add_atribute(self, name, atribute)

    Arguments:
        name {str} -- the value is str
        atribute {str} -- the value is str

    Raises:
        TypeError: can't add new attribute
    """
    try:
        self.name = atribute
    except:
        raise TypeError("can't add new attribute")
