"""
This File contains Classes:
AbstractedLinkedList Class
EasyLinkedList Class
LinkedListRepresentation Class
LinkedList Class
DoublyLinkedList Class
"""
from abc import ABC, abstractmethod, ABCMeta
from typing import Union, Any
from nodes import Node, DoublyNode
from sorting import InsertSort
from linkedlist_iterator import LinkedListIterator
from linkedlist_node_validators import StrictValidator

class AbstractedLinkedList(ABC):
    """
    Used as an Abstract Class for implmenting LinkedList

    Attributes:
        - symbol (str): Is the symbol at which will represent the linked list connection.
    """
    # Representation Symbol
    symbol: str

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

    
class EasyLinkedList(ABC):
    """
    Is a Class to make iterations easier and applicable with Linkedlis.
    The purpose of this class is mainly made to make the linked list support <for loops>.
    This class adds the ability to easily iterate through linked list using for loops
    Also Adds the ability to return a Set Copy or List copy of the linked list where the elements are (node.value).
    """
    
    def to_set(self) -> set:
        """
        Method used to return a set copy of the linked list

        Returns:
            - Python Set
        """
        return {getattr(node, "value", None) for node in self}
    
    def to_list(self) -> list:
        """
        Method used to return a list copy of the linked list

        Returns:
            - Python list
        """
        return [getattr(node, "value", None) for node in self]
    

    # Other dunder methods
    def __len__(self) -> int:
        """
        Dunder Method used to return the length of the linkedlist

        Returns:
            - Length of the linkedlist
        """
        # Store Length
        length: int = 0

        # Loop over the nodes
        for node in self:
            length += 1
        
        return length
    
    # Interation dunder Method
    def __iter__(self) -> LinkedListIterator:
        """
        Dunder Method Allows iteration over the linked list

        Returns:
            - LinkedListIterator
        """
        return LinkedListIterator(self.head)
 
class LinkedListRepresentation(AbstractedLinkedList, EasyLinkedList):
    """
    Class that utilizes the capability of using for loop with linked list to return suitable representation\
    of the linkedlist
    """
    # Representation Methods
    def __repr__(self) -> str:
        """
        Dunder Method used to return represenation of the head node of the linked list

        Returns:
            - String repr of head
        """
        return self.symbol.join(str(node) for node in self)
    
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
    
class LinkedList(LinkedListRepresentation, StrictValidator):
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
    def head(self) -> object:
        """
        Property Method user to return head of the linked list.

        Returns:
            - Head of the linked list can be of Node type of None.
        """
        return self._head

    @head.setter
    def head(self, new: object) -> None:
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

    # Find indexOf
    
    # Drop/pop/Delete method

    # Return Copy Methods
         
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
copy_list: list = new_list.to_list()
copy_set: set = new_list.to_set()

print(type(copy_list)," ", copy_list)
print(type(copy_set)," ", copy_set)
print(type(copy_list[0]))
print(len(new_list))

try:
    obj = EasyLinkedList()
except TypeError as e:
    print(f"TypeError: {e}")