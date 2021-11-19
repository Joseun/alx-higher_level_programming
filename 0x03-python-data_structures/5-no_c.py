#!/usr/bin/python3
def no_c(my_string):
    n = len(my_string)
    for i in range(0, n):
        if my_string[i] != 67 or my_string[i] != 99:
            print("{:s}".format(my_string[i]), end="")
    print('')
            
