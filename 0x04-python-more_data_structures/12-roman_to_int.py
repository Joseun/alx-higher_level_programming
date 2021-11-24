#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_list = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_keys = list(roman_list)
    numerals = []
    if len(roman_string) > 0:
        for i, j in zip(roman_string, roman_keys):
            if i == j:
                numerals.append(roman_list[i])
        decimals = 0            
        for i in range(len(numerals)):
            if i < len(numerals):
                if numerals[i] < numerals[i + 1]:
                    decimals = (numerals[i] * -1) + numeral[i + 1]
                else:
                    decimals += numeral[i]
        return decimals
