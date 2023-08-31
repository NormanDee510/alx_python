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
