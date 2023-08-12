#!/usr/bin/python3
"""python inheritance.

defines and assigns value for parameter

"""
class GeometryMetaClass(type):
    """
    documentation
    """
    def dir(cls):
        return [attribute for attribute in super().dir() if attribute != 'init_subclass']


class BaseGeometry(metaclass=GeometryMetaClass):
    """
    defines and assigns value for parameter
    """

    def dir(cls):
        return [attribute for attribute in super().dir() if attribute != 'init_subclass']
