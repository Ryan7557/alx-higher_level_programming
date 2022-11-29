#!/usr/bin/python3
for cha in range(26):
    if cha != 4 and cha != 16:
        print("{:s}".format(chr(cha + ord("a"))), end="")
