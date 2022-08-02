#!/usr/bin/python3
"""
1-my_list module
Creates a class inheriting from the list class.
"""


class MyList(list):
    """Class MyList inherits from list."""

    def print_sorted(self):
        """Prints the list, in ascending sort."""

        print(sorted(self))
