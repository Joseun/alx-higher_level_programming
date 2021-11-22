#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n = len(tuple_a)
    m = len(tuple_b)
    new_tuple = [0, 0]
    for i in range(2):
        if n > i:
            new_tuple[i] += tuple_a[i]
        else: 0
        if m > i:
            new_tuple[i] += tuple_b[i]
        else: 0
    return tuple(new_tuple)
