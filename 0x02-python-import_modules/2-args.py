#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.", end=" ")
        print('')
    elif len(sys.argv) == 2:
        print("1 argument:", end="")
        print('')
        print("1: {:s}".format(sys.argv[1]), end="")
        print('')
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1), end="")
        print('')    
        for i in range(1, len(sys.argv)):
            if i < len(sys.argv):
                print("{:d}: {:s}".format(i, sys.argv[i]), end="")
                print('')
