#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the max number in a list

    Args: List

    Return: Max integer in List
    """
    if not my_list or len(my_list) == 0:
        return None

    max = 0
    for el in my_list:
        if el > max:
            max = el

    return max
