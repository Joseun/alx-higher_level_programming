#!/usr/bin/python
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            index += 1
        except IndexError:
            raise
        except:
            pass
    print()
    return index
