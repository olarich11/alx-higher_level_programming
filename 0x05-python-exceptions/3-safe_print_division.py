#!/usr/bin/python3

def print_result(result):
    try:
        print("Inside result: {}".format(result))
    except:
        pass

def safe_print_division(a, b):
    try:
        div = a / b
    except (ZeroDivisionError, TypeError):
        div = None
    finally:
        print_result(div)
        return div
