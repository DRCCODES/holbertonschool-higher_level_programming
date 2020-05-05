#!/usr/bin/env python3
def no_c(my_string):
    cpy = ""
    for char in my_string:
        if char is not "C" and char is not "c":
            cpy += char
    return(cpy)
