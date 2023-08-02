#!/usr/bin/python3
"""python inheritance.

defines and assigns value for parameter

"""
class BaseGeometry:
    """ My BaseGeometry class. """

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the 'value' argument.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the 'value' is not an integer.
            ValueError: If the 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")