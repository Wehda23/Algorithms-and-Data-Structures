"""
This File contains Classes:
LinkedListIterator Class
AbstractedLinkedList Class
LinkedList Class
DoublyLinkedList Class
"""
from abc import ABC, abstractmethod
from typing import NoReturn, Union, Any
from nodes import Node, DoublyNode
from convert import LinkedListToList, LinkedListToSet, LinkedListToDict
from sorting import InsertSort

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


class AbstractedLinkedList(ABC):
    """
    Used as an Abstract Class for implmenting LinkedList
    """

    # Which Nodes or type of Nodes are only allowed in the linked list
    allowed_type: object = None
    # Representation Symbol
    symbol: str

    def validate_node(self, node: object) -> Union[None, NoReturn]:
        """
        Validation method used to raise an errror if the type of the node is not a match to the allowed type of Node

        Raises:
            - TypeError: Incase there is a mismatch between the allowed types of Node in the class and Node inserted.

        Args:
            - node: New Node to be validated in the LinkedList
        """
        if not type(node) == self.allowed_type:
            raise TypeError(
                f"""node: Parameter should be of at least one of the following types {str(self.allowed_type)}"""
            )

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

    # String representation
    def __str__(self) -> str:
        """
        Dunder Method used to return a human readable string representation

        Returns:
            - String
        """
        string: str = "[{}]".format(
            ", ".join(str(getattr(node, "value", None)) for node in self)
        )
        return string
    # Other dunder methods
    def __len__(self) -> int:
        """
        Dunder Method used to return the length of the linkedlist

        Returns:
            - Length of the linkedlist
        """
        pass
    
    def __set__(self) -> set:
        """
        Dunder Method user to return copy of the linked list as in set

        Returns:
            - Python Set Data type
        """
        return
    
    def __list__(self) -> list:
        """
        Dunder Method user to return copy of the linked list as in list

        Returns:
            - Python List Data type
        """
        return
    
class LinkedList(AbstractedLinkedList):
    """
    Class that represents a linked list.

    [value, next] - > [value, next] -> [value, next] -> [value, next] -> None
    ^
    Head
    Can Traverse Forwards only.
    """

    # Set an allowed type of Nodes for this class
    allowed_type: Node = Node
    # Traverse Symbol
    symbol: str = " -> "

    def __init__(self, value: Union[int, None] = None) -> None:
        """
        Initializes the Linked List with no elements in it.

        Args:
            - value (int | None): Parameter used to pass in the value of the node Type to set as head of linked list (default: None)
        """
        # Create head node of the linkedlist
        if value is not None:
            node: Node = self.create_node(value)
        else:
            node = None

        self.head: Union[
            Node, None
        ] = node  # Initialize empty list or set head to given value

    @property
    def head(self) -> "LinkedList.allowed_type":
        """
        Property Method user to return head of the linked list.

        Returns:
            - Head of the linked list can be of Node type of None.
        """
        return self._head

    @head.setter
    def head(self, new: "LinkedList.allowed_type") -> None:
        """
        Property Setter Method used to set new head to the linked list.

        Raises:
            - TypeError: incase the type of the node is not amongst the allowed types of the class

        Args:
            - new (LinkedList.allowed_type | None): to set as the new head of the linked list

        Returns:
            - Nothing
        """
        # Validate new in case it is not None
        if new is not None:
            self.validate_node(new)

        # set head to new value
        self._head: Union[Node, DoublyNode, None] = new

    # Create Node Method
    @staticmethod
    def create_node(value: int, *args, **kwargs) -> Node:
        """
        Method used to create a new node
        """
        return Node(value)

    # Add Nodes method
    def add(self, node: Node) -> None:
        """
        Method used to add a node at the end of the linked list.

        Args:
            - node (Node): Should be of type class Node.

        Raises:
            - TypeError: incase the type of the node is not amongst the allowed types of the class

        Returns:
            - Nothing.
        """
        # Define a current pointer
        current: Node = self.head
        # Iterate through the LinkedList till we reach the last element or NULL
        while current.next:
            # Traverse forward
            current: Node = current.next

        # Explanation there is an implementation inside class node to already validate connecting to new node.
        current.next: Node = node

    def push(self, node: Node) -> None:
        """
        Method used to add a node at the start of the linked list and restate the head to this node.

        Args:
            - node (Node): Should be of type class Node.

        Raises:
            - TypeError: incase the type of the node is not amongst the allowed types of the class

        Returns:
            - Nothing.
        """
        # Set node.next = self.head
        node.next = self.head
        # Restate the new head to the node
        self.head: Node = node

    # Drop/pop/Delete method

    # Return Copy Methods

    # Dunder/Magic Methods
    def __iter__(self) -> Node:
        """
        Iteration Dunder Method to go to next node
        """
        return LinkedListIterator(self.head)

    # Representation Methods
    def __repr__(self) -> str:
        """
        Dunder Method used to return represenation of the head node of the linked list

        Returns:
            - String repr of head
        """
        return self.symbol.join(str(node) for node in self)


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
    # Traverse Symbol
    symbol: str = " <-> "

    def __init__(self, value: Union[int, None] = None):
        """
        Initializes the Linked List with no elements in it.

        Args:
            - value (int | None): Parameter used to pass in the value of the node Type to set as head of linked list (default: None)
        """
        super().__init__(value)
        # set the  tail as head.
        self.tail: Union[DoublyNode, None] = self.head

    # Property
    @property
    def tail(self):
        """
        Property Method used to return Tail of the linked list

        Returns:
            - Returns the tail of the linked list.
        """
        return self._tail

    @tail.setter
    def tail(self, new_node: DoublyNode):
        """
        Property Setter Method used to set a new node as tail of linked list

        Raises:
            - TypeError: In case the type of the node is not None or DoublyNode

        Args:
            - new_node (DoublyNode): Should be of type DoublyNode or None.
        """
        if new_node is not None:
            self.validate_node(new_node)
        self._tail: Union[DoublyNode, None] = new_node

    # Creating Node Method
    @staticmethod
    def create_node(value: int, *args, **kwargs) -> DoublyNode:
        """
        Method used to create a new node
        """
        return DoublyNode(value)

    # Add method
    def add(self, node: DoublyNode) -> None:
        pass

    def push(self, node: DoublyNode) -> None:
        pass


node: Node = Node(10)
node2: Node = Node(15)
new_list: LinkedList = LinkedList(10)
new_list.add(node)
new_list.add(node2)
node3: Node = new_list.create_node(22)
new_list.add(node3)

print(new_list)
