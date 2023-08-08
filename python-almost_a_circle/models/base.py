#!/usr/bin/env python3
"""
Module documentation: Base
"""

class Base:
    """
    The Base class for managing the id attribute.
    """

    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
            id (int): Optional ID for the instance.

        Attributes:
            id (int): The public instance attribute representing the ID.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects