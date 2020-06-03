#!/usr/bin/python3
""" create pbj from JSON """


import json


def load_from_json_file(filename):
    """ creats obj from JSON """

    with open(filename) as f:
        return (json.load(f))
