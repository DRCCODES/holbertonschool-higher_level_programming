#!/usr/bin/python3
""" Docs for MyInt inheriates from int """


class MyInt(int):
    """ Class MyInt inherites from int """

    def __init__(self, value):
        """ inits self and value """

        self.value = value

    def __ne__(self, item):
        """ overrides != to == """

        return self.value == item

    def __eq__(self, item):
        """ overrides == to != """

        return self.value != item
