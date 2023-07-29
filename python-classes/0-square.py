class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        self.__size = size

    def dict_(self):
        """
        Get a dictionary representation of the square.

        Returns:
            dict: A dictionary containing the square attributes.
        """
        return {'size': self.__size}

    def get_size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size


if __name__ == "__main__":
    # Test cases
    mysquare = Square(3)
    print(type(mysquare))
    print(mysquare.dict_())

    mysquare = Square(89)
    print(type(mysquare))
    print(mysquare.dict_())

    try:
        print(mysquare.size)
    except AttributeError as e:
        print(e)

    try:
        print(mysquare._size)
    except AttributeError as e:
        print(e)