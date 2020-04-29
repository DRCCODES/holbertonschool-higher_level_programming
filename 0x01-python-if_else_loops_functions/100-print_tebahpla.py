#!/usr/bin/python3
up = 0
for i in range(122, 96, -1):
    if up > 0:
        cap = i - 32
        print("{:c}".format(cap), end="")
        up = 0
    else:
        cap = i
        print("{:c}".format(cap), end="")
        up = 1
