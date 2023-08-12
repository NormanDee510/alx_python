#!/usr/bin/python3
"""python inheritance.

defines and assigns value for parameter

"""
class BaseGeometry:
    def __dir__(cls) -> None:
        # get list of all attributes for this class and exclude __init_subclass
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']