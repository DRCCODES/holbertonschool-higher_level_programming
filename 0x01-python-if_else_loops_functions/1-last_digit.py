#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number
if ld < 0:
    ld = (ld * -1) % 10
else:
    ld = ld % 10
if number < 0 and ld != 0:
        print("Last digit of {:d} is {:d} and\
 is less than 6 and not 0".format(number, ld * -1))
elif ld == 0:
        print("Last digit of {:d} is {:d} and\is 0".format(number, ld))
elif ld > 0:
    if ld < 6:
        print("Last digit of {:d} is {:d} and\
 is less than 6 and is not 0".format(number, ld))
    elif ld > 5:
        print("Last digit of {:d} is {:d} and\
 is greater than 5 and is not 0".format(number, ld))
