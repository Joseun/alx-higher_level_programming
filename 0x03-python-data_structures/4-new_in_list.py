#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    new_list = my_list[:]
    if idx < 0 or idx > n - 1:
        return new_list
    for i in range(0, n):
        if i == idx:
            new_list[i] = element
            return new_list
