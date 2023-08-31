"""python inheritance.

defines and assigns value for parameter

"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


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

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
    