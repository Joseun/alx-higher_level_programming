#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    n = len(my_list)
    max_value = my_list[0]
    if n > 1:
        for i in range(n):
            if i < n:
                if my_list[i] < my_list[i + 1]:
                    max_value = my_list[i + 1]
                elif my_list[i] > my_list[i + 1]:
                    max_value = my_list[i]
                return max_value
    else:
        return max_value
