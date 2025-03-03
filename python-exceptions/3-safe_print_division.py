#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        try:
            result = a / b
            print("Inside result: {}".format(result))
        except:
            result = None
            print("Inside result: {}".format(result))
    finally:
        return result
