"""python inheritance.

defines and assigns value for parameter

"""
class MetaGeometry(type):
    """this class overrides the dir init subclass in the class"""

def __dir__(cls):
    """Magic method that allows to override default"""
class BaseGeometry:
    """ My BaseGeometry class. """

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")