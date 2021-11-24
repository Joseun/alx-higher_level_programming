#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    if len(my_list) > 0:
        for i, j in enumerate(my_list):
            if j == search:
                new_list[i] = replace
        return new_list
    else:
        return my_list
            
