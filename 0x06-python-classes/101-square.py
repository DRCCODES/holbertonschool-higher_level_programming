#!/usr/bin/python3
""" Doc for Class Square!"""


class Square():

    """Square has 4 sides"""

    def __init__(self, size=0, position=(0, 0)):

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

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):

        "returns posistion"
        return self.__position

    @position.setter
    def position(self, value):

        "sets position to value"
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):

        """finds area of a square"""

        return self.__size ** 2

    def my_print(self):

        """prints equal sized sided square"""
        if self.__size == 0:
            print()
            return

        for s in range(self.__position[1]):
            print()

        for row in range(self.__size):
            for lines in range(self.__position[0]):
                print(" ", end='')
            for columns in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        sq = []

        if self.__size == 0:
            return ""

        for s in range(self.__position[1]):
            sq.append("\n")

        for row in range(self.__size):
            for lines in range(self.__position[0]):
                sq.append(" ")
            for columns in range(self.__size):
                sq.append("#")
            if row != self.size - 1:
                sq.append("\n")
        return ''.join(sq)
