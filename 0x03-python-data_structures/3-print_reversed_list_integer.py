#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return
    n = len(my_list) - 1
    if n == 0:
        return
    else:
        for i in range(n, 0, -1):
            print("{:d}".format(my_list[i]))
        print("{:d}".format(my_list[0]))
