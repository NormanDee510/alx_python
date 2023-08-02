#!/usr/bin/python3
"""python inheritance.

defines and assigns value for parameter

"""
def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited from the specified class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class



