#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    n = list(a_dictionary)
    for i in n:
        if i == key:
            del a_dictionary[i]
    return a_dictionary
       # else:
        #    return a_dictionary
