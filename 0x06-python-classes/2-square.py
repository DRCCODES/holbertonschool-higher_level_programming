#!/usr/bin/python3
""" Doc for Class Square!"""


class Square:

    """Square has 4 sides"""

    def __init__(self, size=0):

        """init of self and size

        Args: are size of type int

        Raise: Exceptions if not int or size < 0

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
