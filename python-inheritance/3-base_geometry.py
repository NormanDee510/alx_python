"""python inheritance.defines and assigns value for parameter"""

class MetaClassGeometry(type):
    """Overrides the dir method in the subclass"""

    def __dir__(cls):
        """Method that overrides default dir"""
        return [
            attribute for attribute in super().__dir__()
            if attribute != '__init_subclass__'
        ]


class BaseGeometry(metaclass=MetaClassGeometry):
    """Defines and assigns value for parameters"""

    def __dir__(cls):
        return [
            attribute for attribute in super().__dir__()
            if attribute != '__init_subclass__'
        ]
