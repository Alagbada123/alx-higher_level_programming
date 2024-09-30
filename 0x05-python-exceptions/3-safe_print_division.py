#!/usr/bin/python3

def safe_print_division(a, b):
    D = None

    try:
        D = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(D))
    return D
