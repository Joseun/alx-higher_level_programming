#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n = list(a_dictionary)
    new_dict = a_dictionary.copy()
    for i in n:
        new_dict[i] = new_dict[i] * 2
    return new_dict 
    
