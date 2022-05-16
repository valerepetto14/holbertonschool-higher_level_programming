#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return None
