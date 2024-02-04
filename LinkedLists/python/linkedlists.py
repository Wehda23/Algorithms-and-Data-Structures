"""
This File contains Classes:
LinkedList Class
DoublyLinkedList Class
"""
from typing import NoReturn, Union, Optional
from nodes import Node, DoublyNode


class LinkedListIterator:
    """
    Class used as a helper to iterate over a linked list
    """

    def __init__(self, head: Union[Node, DoublyNode]):
        """
        Initializes an iterator object with the given node.

        Args:
            - head: Pointer to the head of the node
        """

        self.current: Union[Node, DoublyNode] = head
    
    def __iter__(self) -> Union[Node, DoublyNode]:
        """
        Dunder Method used during iterations
        """
        return self

    def __next__(self) -> None:
        """
        Method Used during iteration to move to next node

        Returns:
            - Node type object.
        """

        # First check if current is not None
        if self.current is None:
            raise StopIteration
        
        node = self.current
        self.current = self.current.next
        return node
        
class LinkedList:
    """
    Class that represents a linked list.

    [value, next] - > [value, next] -> [value, next] -> [value, next] -> None
    ^
    Head
    Can Traverse Forwards only.
    """

    # Set an allowed type of Nodes for this class
    allowed_type: Node = Node

    def __init__(self, node: Union[Node, DoublyNode, None] = None) -> None:
        """
        Initializes the Linked List with no elements in it.

        Args:
            - node (Node, DoublyNode, None): Parameter used to pass in the Node Type to set as head of linked list (default: None)
        """
        self.head: Union[
            Node, DoublyNode, None
        ] = node  # Initialize empty list or set head to given value

    @property
    def head(self) -> Union[Node, DoublyNode, None]:
        """
        Property Method user to return head of the linked list.

        Returns:
            - Head of the linked list can be of Node type of None.
        """
        return self._head

    @head.setter
    def head(self, new: Union[Node, DoublyNode, None]) -> None:
        """
        Property Setter Method used to set new head to the linked list.

        Raises:
            - TypeError: incase the type of the node is not amongst the allowed types of the class

        Args:
            - new (Node | DoublyNode | None): to set as the new head of the linked list

        Returns:
            - Nothing
        """
        # Validate new in case it is not None
        if new is not None:
            self.validate_head(new)

        # set head to new value
        self._head: Union[Node, DoublyNode, None] = new

    def validate_head(self, head: Union[Node, DoublyNode]) -> Union[None, NoReturn]:
        """
        Validation Method used to validate head input

        Raises:
            - TypeError: incase the type of the node is not amongst the allowed types of the class

        Returns:
            - Nothing.
        """

        if not type(head) == self.allowed_type:
            raise TypeError(
                f"""head: Parameter should be of at least one of the following types {str(self.allowed_type)}"""
            )
    # Add Nodes method


    # Sort Node Method
    
    # Return Copy Methods
    
    # Dunder/Magic Methods
    def __iter__(self) -> Node:
        """
        Iteration Dunder Method to go to next node
        """
        return LinkedListIterator(self.head)
    
    # Representation Methods
    def __str__(self) -> str:
        """
        Dunder Method used to return a human readable string representation

        Returns:
            - String
        """
        return " -> ".join(repr(node) for node in self)
    
    def __repr__(self) -> str:
        """
        Dunder Method used to return represenation of the head node of the linked list

        Returns:
            - String repr of head
        """
        return repr(self.head)

class DoublyLinkedList(LinkedList):
    """
    Class That represents a doubly linked list
    None <- [previous, value, next] < - > [previous, value, next] < - > [previous, value, next] < - > [previous, value, next] - > None
            ^                                                                                         ^
            Head                                                                                      Tail
    Can Travers Backwards and Forwards.
    """

    # Set an allowed type of Nodes for this class
    allowed_type: DoublyNode = DoublyNode


node: Node = Node(10)
node2: Node = Node(15)
node.next = node2
new_list: LinkedList = LinkedList(node)


print(new_list)
