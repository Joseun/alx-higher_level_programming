#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    n = list(a_dictionary)
    best_key = n[0]
    if len(n) > 1:
        for i in n:
            if a_dictionary[i] > a_dictionary[best_key]:
                best_key = i
        return best_key
    
