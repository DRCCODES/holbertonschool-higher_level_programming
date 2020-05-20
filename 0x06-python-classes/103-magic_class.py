#!/usr/bin/python3


import math


""" Magic Calculator """


class MagicClass:

    def __init__(self, radius):

        """get radius"""

        self.radius = 0

        if type(radius) is not float and is not int:
            raise TypeError("radius must be a number")

        self.radius = radius

    def area(self):

        """ Get area! """

        return math.pi * (self.__radius ** 2)

    def circumference(self):

        """ Get Circumference """

        return 2 * math.pi * self.__radius
