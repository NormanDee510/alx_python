#!/usr/bin/env python3
"""
Module documentation: Square
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            id (int): Optional ID for the instance.

        Attributes:
            size (int): The size of the square (width and height).
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The public instance attribute representing the ID.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size (width/height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size (width/height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: A formatted string representing the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)