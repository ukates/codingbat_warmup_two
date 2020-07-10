"""Given a string and a non-negative int n,
return a larger string that is n copies of the original string."""


def string_times(str, n):
    return str * n


# return n copies of front 3 items of string

def front_times(str, n):
    if len(str) <= 3:
        return str * n
    return str[:3] * n


# return new string made of every other char starting with first

def string_bits(str):
    new_str = ''
    is_other = True
    for char in str:
        if is_other:
            new_str += char
            is_other = False
        else:
            is_other = True
    return new_str


# Given a string like 'Code' return a string like 'CCoCodCode'

def string_splosion(str):
    new_str = ''
    for i in range(len(str)):
        new_str += str[:i + 1]
    return new_str


# Return the count of the number of times a substring len 2 appears in the string,
# also, as the last 2 chars of the string, so "hixxxhi" yields 1, we dont count the end substring

def last2(str):
    if len(str) < 2:
        return 0
    last2 = str[len(str) - 2:]
    count = 0
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == last2:
            count = count + 1

    return count
