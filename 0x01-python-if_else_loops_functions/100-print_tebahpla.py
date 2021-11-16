#!/usr/bin/python3
for i in range(122, 96):
        if ord(i) in range(121, 96, 2):
                i = chr(ord(i) - 32)
                print ("{:s}".format(i), end = "")
                print ('')

