#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for num in range(0, x):
        try:
            print(my_list[num], end="")
        except IndexError:
            print()
            return num
    print()
    return num + 1
