"""
Problem Set 1.2
"""


# Problem 1: Integer Replacement
def replace_integer(n: int) -> int:
    """
    Given a positive integer n, you can apply one of the following operations:
    - If n is even, replace n with n / 2.
    - If n is odd, replace n with either n + 1 or n - 1.
    - Return the minimum number of operations needed for n to become 1.

    Parameters:
        n (int): positive integer

    Returns:
        int: minimum number of operations needed for n to become 1
    """
    
    def replace(n: int, num_operations: int):
        if n == 1:
            return num_operations
        elif n % 2 == 0:
            return replace(n // 2, num_operations + 1)
        else:
            return min(replace(n + 1, num_operations + 1), replace(n - 1, num_operations + 1))

    return replace(n, 0)

# n = 8
# print(replace_integer(n))

# n = 7
# print(replace_integer(n))

# n = 4
# print(replace_integer(n))


# Problem 2: Roman to Integer
def roman_to_integer(s: str) -> int:
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol Value I 1 V 5 X 10 L 50 C 100 D 500 M 1000
    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. X can be placed before L (50) and C (100) to make 40 and 90. C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.

    Parameters:
        s (str): Roman numeral

    Returns:
        int: integer form of Roman numeral
    """
    number = 0
    before = None

    for c in s:
        if c == 'I':
            if before == 'I':
                number += 2
                before = None
            elif before == 'X':
                number += 10
                before = 'I'
            elif before == 'C':
                number += 100
                before = 'I'
            else:
                before = 'I'
        elif c == 'V':
            if before == 'I':
                number += 4
                before = None
            elif before == 'X':
                number += 15
                before = None
            elif before == 'C':
                number += 105
                before = None
            else:
                number += 5
        elif c == 'X':
            if before == 'I':
                number += 9
                before = None
            elif before == 'X':
                number += 20
                before = None
            elif before == 'C':
                number += 100
                before = 'X'
            else:
                before = 'X'
        elif c == 'L':
            if before == 'X':
                number += 40
                before = None
            elif before == 'C':
                number += 150
                before = None
            else:
                number += 50
        elif c == 'C':
            if before == 'X':
                number += 90
                before = None
            elif before == 'C':
                number += 200
                before = None
            else:
                before = 'C'
        elif c == 'D':
            if before == 'C':
                number += 400
                before = None
            else:
                number += 500
        elif c == 'M':
            if before == 'C':
                number += 900
                before = None
            else:
                number += 1000
    
    if before == 'I':
        return number + 1
    elif before == 'X':
        return number + 10
    elif before == 'C':
        return number + 100
    else:
        return number

# s = "III"
# print(roman_to_integer(s))

# s = "LVIII"
# print(roman_to_integer(s))

# s = "MCMXCIV"
# print(roman_to_integer(s))


# Problem 3: Integer to Roman
def integer_to_roman(num: int) -> str:
    nums = {
        1: "I",
        5: "V", 4: "IV",
        10: "X", 9: "IX",
        50: "L", 40: "XL",
        100: "C", 90: "XC",
        500: "D", 400: "CD",
        1000: "M", 900: "CM"
    }

    s = ""

    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        while n <= num:
            s += nums[n]
            num -= n
    
    return s

# num = 3749
# print(integer_to_roman(num))

# num = 58
# print(integer_to_roman(num))

# num = 1994
# print(integer_to_roman(num))
