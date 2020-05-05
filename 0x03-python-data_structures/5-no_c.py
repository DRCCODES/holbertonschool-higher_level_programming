#!/usr/bin/env python3
def no_c(my_string):
    cpy = ""
    for char in my_string:
        if char == "C" or char == "c":
            char = ""
        cpy += char
    return(cpy)
