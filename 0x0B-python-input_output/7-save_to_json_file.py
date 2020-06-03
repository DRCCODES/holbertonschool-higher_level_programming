#!/usr/bin/python3
""" writes obj to txt using json rep """


import json


def save_to_json_file(my_obj, filename):
    """ obj writen to txt json rep """

    with open(filename, mode="w") as f:
        f.write(json.dumps(my_obj))
