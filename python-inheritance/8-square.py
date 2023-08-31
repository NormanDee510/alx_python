#!/usr/bin/python3
"""python inheritance.

defines and assigns value for parameter

"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """ My Square class that inherits from Rectangle. """

    def __init__(self, size):
        """Instantiates the Square with size."""        
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the Square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
        