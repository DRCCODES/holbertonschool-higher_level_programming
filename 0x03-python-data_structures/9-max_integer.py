#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        return None
    for i in range(size - 1):
        for j in range(0, size - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j+1], my_list[j]
    return (my_list[size - 1])
