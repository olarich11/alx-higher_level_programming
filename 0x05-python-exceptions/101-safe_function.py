#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as i:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
