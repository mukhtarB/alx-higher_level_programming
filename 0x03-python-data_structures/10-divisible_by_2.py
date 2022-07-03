#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Check if items are divisible by 2

    Args: a List item

    Return: A new boolean list for each item
    """

    if len(my_list) == 0:
        return

    new_list = []
    for el in my_list:
        new_list.append(True) if el % 2 == 0 else new_list.append(False)

    return new_list
