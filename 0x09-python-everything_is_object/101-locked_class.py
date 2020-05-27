#!/usr/bin/python3
"""101-locked_class
    """


class LockedClass:
    """Lockedclass
    """
    __slots__ = "first_name"

    def __init__(self, first_name=""):
        """[__init__

        Keyword Arguments:
            first_name {str} -- first_name (default: {""})
        """
        self.first_name = first_name
