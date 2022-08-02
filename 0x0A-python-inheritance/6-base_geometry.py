#!/usr/bin/python3
"""
6-base_geometry module
Creates a class.
"""


class BaseGeometry:
    """Class with public instance method."""

    def area(self):
        """Raises an Exception when area is not defined

        Raises:
            Exception: area not implemented
        """

        raise Exception('area() is not implemented')
