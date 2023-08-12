#!/usr/bin/python3
class BaseGeometry(type):
    """ My BaseGeometry class. """

    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=BaseGeometry):
    """
    documentation for class goes here
    """
    
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']