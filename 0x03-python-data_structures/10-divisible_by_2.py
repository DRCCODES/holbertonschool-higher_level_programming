#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bytwo = []
    for num in my_list:
        if num % 2 == 0:
            bytwo.append(True)
        else:
            bytwo.append(False)
    return bytwo
