#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    n = len(my_list)
    new_list = []
    if idx < 0 or idx > n - 1:
        new_list = my_list
    else:
        for i in range(n):
            if i is not idx:
                new_list.append(my_list[i])
        my_list = new_list
        return my_list
