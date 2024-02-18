"""
File that contains abstracted Nodes
"""
from abc import ABC, abstractmethod
from typing import Union


class AbstractedForwardNode(ABC):
    """
    Abstracted Node class that ensures node travereses forwards
    """

    @abstractmethod
    def next(self) -> Union["AbstractedForwardNode", None]:
        """
        Method used to point this node to another of same type or None

        Returns:
            - Node or None.
        """
        pass


class AbstractedBackwardNode(ABC):
    """
    Abstracted BackwardNode class
    """

    @abstractmethod
    def previous(self) -> Union["AbstractedBackwardNode", None]:
        """
        Method used to point this node to another of same type or None

        Returns:
            - Node or None.
        """
        pass
