#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n = len(tuple_a)
    m = len(tuple_b)
    if n < 2:
    for i in range(n + 1):
        if tuple_a[i] == None:
    tuple_a[i] = 0       
    for i in range(m):
        if tuple_b[i] == None:
            tuple_b[i] = 0
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    new_tuple = a, b
    return new_tuple
