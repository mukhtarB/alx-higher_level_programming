#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print matrix of integers

    Args: matrix: a 2d list

    Return: None
    """
    for list_el in matrix:
        for list_item in list_el:
            if list_item != list_el[-1]:
                print("{:d}".format(list_item), end=" ")
            else:
                print("{:d}".format(list_item), end="")
        print('')
