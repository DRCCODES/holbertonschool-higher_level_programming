#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        re = fct(*args)
        return re
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
