"""python inheritance.

defines and assigns value for parameter

"""
class MetaGeometry(type):
    """This class overrides the dir init subclass in the class"""

    def __dir__(cls):
        """Magic method that allows to override default"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=MetaGeometry):
    """My BaseGeometry class."""

    def __dir__(cls):
        """Magic method that allows to override default"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
       

    def integer_validator(self, name, value):
        """Validates the 'value' argument"""       
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
