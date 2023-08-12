#!/usr/bin/python3
"""
python inheritance.
defines and assigns value for parameter

"""
class GeometryMetaClass(type):
    """
    Overides the dir init subclass in the class
    """
    def __dir__(cls):
        """ Method that overide default dir"""
        return (attribute for attribute in super().__dir__() if attribute != 'init_subclass')


class BaseGeometry(metaclass=GeometryMetaClass):
    """
    defines and assigns value for parameter
    """

    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != 'init_subclass']
