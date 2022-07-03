#!/usr/bin/python3
def no_c(my_string):
    """Remove all 'c' and 'C' char from string.

    Args: my_string: str to remove from

    Return: new string
    """
    new_string = ''
    for character in my_string:
        if character not in 'cC':
            new_string += character
    return new_string
