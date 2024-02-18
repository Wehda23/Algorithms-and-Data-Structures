"""
File that contains Node validators
"""
from python_lists.validators import AbstractNodeValidator


class NodeValidator(AbstractNodeValidator):
    """
    Class for node validation
    """

    def validate_node(self, node: object) -> None:
        """
        Class Method used to validate the value will raise error incase of failure

        Args:
            - node ({__class__} | None): Typeclass {__class__}

        Raises: TypeError incase of error

        Returns:
            - Nothing
        """

        # Check type of next
        if not (type(node) == self.__class__):
            raise TypeError(f"node: Should be of type {self.__class__.__name__}.")
