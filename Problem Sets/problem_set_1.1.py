"""
Problem Set 1.1
"""


# Problem 1: Substring
def substring(str1: str, str2: str) -> bool:
    """
    Write a function that takes in two strings and returns True if the second string is a substring of the first, and False otherwise.
    
    Parameters:
        str1 (str): string
        str2 (str): string
    
    Returns:
        bool: whether second string is substring of first
    """

    str2len = len(str2)

    for i in range(len(str1) - str2len):
        for j in range(str2len):
            if str1[i + j] == str2[j]:
                if j == (str2len - 1):
                    return True
            else:
                break
    
    return False

# str1 = "laboratory"
# str2 = "rat"
# print(substring(str1, str2))

# str1 = "cat"
# str2 = "meow"
# print(substring(str1, str2))


# Problem 2: Longest Common Prefix
def longest_common_prefix(strs: list[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
    
    Parameters:
        strs (list[str]): list of strings
    
    Returns:
        str: longest common prefix
    """

    length = min(len(str) for str in strs)
    prefix = ""

    for i in range(length):
        character = strs[0][i]
        for s in strs[1:]:
            if s[i] != character:
                return prefix
        prefix += character

    return prefix

# strs = ["flower", "flow", "flight"]
# print(longest_common_prefix(strs))

# strs = ["dog", "racecar", "car"]
# print(longest_common_prefix(strs))


# Problem 3: Add Binary
def add_binary(a: str, b: str) -> str:
    """
    Given two binary strings a and b, return their sum as a binary string.
    
    Parameters:
        a (str): binary string
        b (str): binary string
    
    Returns:
        str: sum of a and b in binary
    """
    
    string = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        string.append(str(carry % 2))
        carry //= 2
    
    return "".join(reversed(string))

# a = "11"
# b = "1"
# print(add_binary(a, b))

# a = "1010"
# b = "1011"
# print(add_binary(a, b))
