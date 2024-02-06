"""
File that contains Two Class:
AbstractedLinkedList Class
AbstractedDoublyLinkedList
"""
from abc import ABC, abstractmethod
from typing import Union, Any


class AbstractedLinkedList(ABC):
    """
    Used as an Abstract Class for implmenting LinkedList
    """
    
    @abstractmethod
    def create_node(value: Any) -> object:
        """
        Staticmethod used to create and return a New Node of the allowed type of Node

        Args:
            - value: Can be any allowed type of value to be stored inside the Node

        Returns:
            - New Node
        """
        pass
    
    @abstractmethod
    def head(self) -> Union[object, None]:
        """
        Method used to return the head of the linked list

        Returns:
            - Node of type <Object> if there is a node in the List else returns None.
        """
        pass

    @abstractmethod
    def index_of(self, value: Any) -> Union[int, None]:
        """
        Method that is supposed to get the index of the node that contains the input value

        Args:
            - value (Any): Target Value.
        
        Returns:
            - Index of the node that contains this value or incase if not found returns None.
        """
        pass
    
    @abstractmethod
    def copy(self) -> "AbstractedLinkedList":
        """
        Method used to return a copy of the linked list

        Returns:
            - Copy of the linkedlist.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Dunder Method used to return a human-readable string representation

        Returns:
            - String
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Dunder Method used to return representation of the head node of the linked list

        Returns:
            - String repr of head
        """
        pass
    
    @abstractmethod
    def __len__(self) -> str:
        """
        Method used to get the length of the linkedlist

        Returns:
            - Length of the linkedlist
        """
        pass



class AbstractedDoublyLinkedList(ABC):
    """
    Abstracted Class to ensure the implementation of requirements to operate as a DoublyLinked List
    """ 

    @abstractmethod
    def tail(self) -> object:
        pass