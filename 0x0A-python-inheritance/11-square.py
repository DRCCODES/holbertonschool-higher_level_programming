#!/usr/bin/python3
""" Square Class inherits Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The Class Square """

    def __init__(self, size):
        """ inits Square size and self """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns area of Square """

        return self.__size ** 2

    def __str__(self):
        """ return for use with print() and str() """

        return "[Square] {}/{}".format(self.__size, self.__size)
