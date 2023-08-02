#!/usr/bin/python3
"""python inheritance.

defines and assigns value for parameter

"""
def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of, or an instance of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class or inherited from it; otherwise, False.
    """
    return isinstance(obj, a_class)