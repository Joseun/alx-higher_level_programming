#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    new_list = my_list[:]
    for i in range(len(my_list)):
        m = my_list[i] % 2
        if m == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
