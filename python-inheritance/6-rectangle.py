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


class Rectangle(BaseGeometry):
    """ My Rectangle class that inherits from BaseGeometry. """

    def __init__(self, width, height):
        """Instantiates the Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"