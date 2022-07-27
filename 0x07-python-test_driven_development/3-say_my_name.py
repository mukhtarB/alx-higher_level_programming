#!/usr/bin/python3
"""
3-say_my_name module
Prints a given first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """"Function that prints a string with
    <first_name> and <last_name>.
    Args:
        first_name (str)
        last_name (str, optional). Defaults to "".
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
