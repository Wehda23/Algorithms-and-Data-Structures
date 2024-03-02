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


class AbstractedRightNode(ABC):
    """
    Abstracted Right Node
    """

    @abstractmethod
    def right(self) -> Union["AbstractedRightNode", None]:
        """
        Method used to point this node to another of same type or None

        Returns:
            - Node or None.
        """
        pass


class AbstractedLeftNode(ABC):
    """
    Abstracted Left Node
    """

    @abstractmethod
    def left(self) -> Union["AbstractedLeftNode", None]:
        """
        Method used to point this node to another of same type or None

        Returns:
            - Node or None.
        """
        pass


class AbstractedParentNode(ABC):
    """
    Abstracted Parent Node
    """

    @abstractmethod
    def parent(self) -> Union["AbstractedParentNode", None]:
        """
        Method used to point this node to another of same type or None

        Returns:
            - Node or None.
        """
        pass
