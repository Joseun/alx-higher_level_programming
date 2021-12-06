#!/usr/bin/python
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "None"
