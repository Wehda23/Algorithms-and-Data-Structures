"""
File that contains linkedlist node validators
"""
from abc import ABC, abstractmethod
from typing import NoReturn, Union

class AbstractLinkedListNodeValidator(ABC):
    """
    Abstract Class showing the LinkedList Node Validator
    """

    @abstractmethod
    def validate_node(self, node: object) -> Union[None, NoReturn]:
        pass

class StrictValidator(AbstractLinkedListNodeValidator):
    """
    This is a class used to strictly validate nodes that are connected in the linked list
    """
    # Which Nodes or type of Nodes are only allowed in the linked list
    allowed_type: object = None

    def check_type(self) -> Union[NoReturn, None]:
        """
        Method used to check if class has attribute called allowed_type
        """
        if not hasattr(self.__class__, "allowed_type") or self.allowed_type is None:
            raise NotImplementedError("The class does not have 'allowed_type' attribute")

    def validate_node(self, node: object) -> Union[None, NoReturn]:
        """
        Validation method used to raise an errror if the type of the node is not a match to the allowed type of Node

        Raises:
            - TypeError: Incase there is a mismatch between the allowed types of Node in the class and Node inserted.

        Args:
            - node: New Node to be validated in the LinkedList
        """
        # Check Type
        self.check_type()

        if not type(node) == self.allowed_type:
            raise TypeError(
                f"""node: Parameter should be of at least one of the following types {str(self.allowed_type)}"""
            )