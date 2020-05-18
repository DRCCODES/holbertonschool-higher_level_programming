#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    size = 0
    for num in range(0, x):
        try:
            print(my_list[num], end="")
            size += 1
        except IndexError:
            break
    print()
    return size
