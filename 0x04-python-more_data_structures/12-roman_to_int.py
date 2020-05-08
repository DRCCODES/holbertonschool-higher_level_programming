#!/usr/bin/python3
def roman_to_int(roman_string):
    rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if type(roman_string) is str:
        curr = 0
        romans = 0
        past = 1000
        goths = 0
        for char in roman_string:
            if char in rome:
                curr = rome[char]
            else:
                return 0

            if curr > past:
                goths += past
                romans += curr
                past = curr
            else:
                romans += curr
                past = curr
        romans = romans - goths * 2
        return romans
    return 0
