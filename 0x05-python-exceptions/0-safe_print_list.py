#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0

    for item in range(0, x):

        try:
            print("{}".format(my_list[item]), end='')

            counter += counter

        except IndexError:
            pass

    print()
    return counter
