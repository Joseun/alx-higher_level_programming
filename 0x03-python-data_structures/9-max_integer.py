#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    max_value = my_list[0]
    if len(my_list) > 1:
        for i in my_list:
            if i > max_value:
                max_value = i
    return max_value
