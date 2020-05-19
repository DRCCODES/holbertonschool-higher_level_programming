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

    @property
    def size(self):

        """ returns size"""

        return self.__size

    @size.setter
    def size(self, value):

        """Sets size to given value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """finds area of a square"""

        return self.__size ** 2

    def my_print(self):

        """prints equal sized sided square"""
        if self.size == 0:
            print()

        for side in range(self.size):
            for oside in range(self.size):
                print("#", end="")
            print()
