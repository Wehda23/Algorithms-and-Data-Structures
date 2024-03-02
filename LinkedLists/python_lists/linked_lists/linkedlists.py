"""
This File contains Classes:
EasyLinkedList Class
LinkedListRepresentation Class
LinkedList Class
DoublyLinkedList Class
"""
from .abstracts import (
    AbstractedLinkedList,
    AbstractedDoublyLinkedList,
)
from .sorting import InsertSort
from .linkedlist_iterator import LinkedListIterator
from .linkedlists_validators import StrictValidator
from typing import Union, NoReturn
from python_lists.nodes.nodes import Node, DoublyNode


class EasyLinkedList:
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

    # Interation dunder Method
    def __iter__(self) -> LinkedListIterator:
        """
        Dunder Method Allows iteration over the linked list

        Returns:
            - LinkedListIterator
        """
        # Check if the class has an attribute called head or not
        if not hasattr(self.__class__, "head"):
            raise TypeError("Class does not have an attribute called 'head'.")

        return LinkedListIterator(self.head)


class LinkedListRepresentation(AbstractedLinkedList, EasyLinkedList):
    """
    Class that utilizes the capability of using for loop with linked list to return suitable representation\
    of the linkedlist
    It is not Recommended to create an instance from this Class.

    Attributes:
        - symbol (str): Is the symbol at which will represent the linked list connection.
    """

    # Representation Symbol
    symbol: str

    def check_symbol(self) -> Union[None, NoReturn]:
        """
        Method to check if the subclass has defined class Attribute Symbol or not
        """
        # Check if class contains self or not
        if not hasattr(self.__class__, "symbol"):
            raise NotImplementedError("Class Attribute 'symbol' must be defined.")

    # Representation Methods
    def __repr__(self) -> str:
        """
        Dunder Method used to return represenation of the head node of the linked list

        Returns:
            - String repr of head
        """
        # Check Symbol
        self.check_symbol()

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

    # ADD or PUSH Methods
    # Methods that Adds an Entire node or pushes it into the linked list
    # The nodes were previously created outside the linkedlist.
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
        # incase of empty list
        if not self.head:
            self.head = node
            return
        # Define a current pointer
        current: Node = self.head
        # Iterate through the LinkedList till we reach the last element or NULL
        while current.next:
            # Traverse forward
            current: Node = current.next

        # Explanation there is an implementation inside class node to already validate connecting to new node.
        current.next = node

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

    # Append & Extend Methods
    # Creates new node with the values inserted.
    def append(self, *args, **kwargs) -> None:
        """
        Method to append the values to linked lists
        This method mainly uses self.add method to add new values
        Args:
            - args(*int): integer values inserted

        Returns:
            - Nothing
        """
        # Check args
        if args:
            for value in args:
                node: object = self.create_node(value)
                self.add(node)
    
    def extends(self, *args, **kwargs) -> None:
        """
        Method to append the values to linked lists
        This method mainly uses self.push method to push new values
        Args:
            - args(*int): integer values inserted

        Returns:
            - Nothing
        """
        # Check args
        if args:
            for value in args:
                node: object = self.create_node(value)
                self.push(node)
        
    # Drop/pop/Delete method
    def pop(self, index: int = 0) -> Node:
        """
        Method used to remove an element from the list and returns it

        Args:
            - index (int): integer identifying at which index this element exists.

        Raises:
            - IndexError: Incase if the index input was outside index of linked list.

        Returns:
            - Object or Node Type
        """
        # Empty list
        if len(self) == 0:
            raise ValueError("Empty List!")
        
        # Check the index
        if index < 0 or index >= len(self):
            raise IndexError("Index is out of bounce")
        
        # incase list has only one element
        if len(self) == 1:
            node: Node = self.head
            self.head = None
            return node
        
        # Pointers
        position: int = 0
        # Grab the head of the linked list
        current: Node = self.head
        temp: Node = self.head.next

        # Loop over the index
        while position < index - 1:
            position += 1
            current = temp
            temp = temp.next
        
        # Remove link
        current.next = temp.next
        temp.next = None
        # Return the node
        return temp

     # Reverse functionalities
    def reverse(self, inplace= True) -> object:
        """
        Function used to reverse linked list

        Args:
            - inplace (bool): parameter which indicates to apply changes to current linked list or not
        
        Returns:
            - Copy of the reversed linked list
        """
        
        # Check inplace
        if not inplace:
            return self.copy(reversed=True)
        
        # first make sure the linked list contains more than one node
        if len(self) <= 1:
            return 
        
        # Pointers
        current: Node = self.head
        next_node: Node = self.head.next
        previous = None

        # Loop
        while current:
            # Save the next node before updating the current.next pointer
            next_node = current.next

            # Reverse the link
            current.next = previous

            # Move the pointers forward
            previous = current
            current = next_node

        # Update the head of the linked list to the last node
        self.head = previous

    def __reversed__(self) -> object:
        """
        Dunder method used to reverse the existing  linked list.
        """
        # Apply reverse function
        self.reverse(inplace=True)
        # Return linked list
        return self
    
    # Below methods are made using the improvements applied by Inherting from EasyLinkedList through multiple inheritance from\
    # LinkedListRepresentation

    # Return Copy Methods
    def copy(self, reversed: bool = False) -> "LinkedList":
        """
        Method that is used to get a copy of the linkedlist.

        Args:
            - reversed (bool): copy and reverse list (default: False)

        Returns:
            - Copy of the linkedlist.
        """
        # Create empty linked list
        copy: "LinkedList" = LinkedList()

        # Iterate over the linked list
        for node in self:
            if reversed:
                copy.push(node.copy())
            else:
                copy.add(node.copy())

        # Return the copied Linkedlist
        return copy
    
    # Find indexOf
    def index_of(self, value: int) -> Union[int, None, NoReturn]:
        """
        Method used to find the first index of the node that contains the target value

        Args:
            - value (int): Integer value to search for in the nodes.
        
        Returns:
            - Index of the node that contains the input value\
                if the value was not found amongst node values\
                it will return None.
        """
        # Check if the linked list is not empty
        if not self.head:
            raise ValueError("Linkedlist is empty!")

        # Loop over the linked list
        for index, node in enumerate(self):
            # Check if the node value matches target value
            if node.value == value:
                # Return the index
                return index

        # Incase the there is no node containing the value returns None
        return None

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

   

class DoublyLinkedList(LinkedList, AbstractedDoublyLinkedList):
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
        """
        Method used to add a node at the end of the linked list.

        Args:
            - node (DoublyNode): Should be of type class DoublyNode.

        Raises:
            - TypeError: incase the type of the node is not amongst the allowed types of the class

        Returns:
            - Nothing.
        """
        # incase of empty list
        if not self.head:
            self.head = node
            return
        # Define a current pointer
        current: Node = self.head
        # Iterate through the LinkedList till we reach the last element or NULL
        while current.next:
            # Traverse forward
            current: Node = current.next

        # Explanation there is an implementation inside class node to already validate connecting to new node.
        current.next = node
        node.previous = current
        # assign as the tail
        self.tail = node

    def push(self, node: DoublyNode) -> None:
        """
        Method used to add a node at the start of the linked list and restate the head to this node.

        Args:
            - node (DoublyNode): Should be of type class DoublyNode.

        Raises:
            - TypeError: incase the type of the node is not amongst the allowed types of the class

        Returns:
            - Nothing.
        """
        # Set node.next = self.head
        node.next = self.head
        # Check first if self.head is a node or none
        if self.head:
            self.head.previous = node
        # Restate the new head to the node
        self.head: DoublyNode = node
        # Make sure previous is a None
        self.head.previous = None

    # Return Copy Methods
    def copy(self, reversed: bool = False) -> "DoublyLinkedList":
        """
        Method that is used to get a copy of the DoublyLinkedList.

        Args:
            - reversed (bool): copy and reverse list (default: False)

        Returns:
            - Copy of the DoublyLinkedList.
        """
        # Create empty linked list
        copy: "DoublyLinkedList" = DoublyLinkedList()

        # Iterate over the linked list
        for node in self:
            if reversed:
                copy.push(node.copy())
            else:
                copy.add(node.copy())

        # Return the copied DoublyLinkedList
        return copy
    
    # Drop/pop/Delete method
    def pop(self, index: int) -> DoublyNode:
        """
        Method used to remove an element from the list and returns it

        Args:
            - index (int): integer identifying at which index this element exists.

        Raises:
            - IndexError: Incase if the index input was outside index of linked list.

        Returns:
            - Object or DoublyNode Type
        """
        # Empty list
        if len(self) == 0:
            raise ValueError("Empty List!")
        
        # Check the index
        if index < 0 or index >= len(self):
            raise IndexError("Index is out of bounce")
        
        # incase list has only one element
        if len(self) == 1:
            node: DoublyNode = self.head
            self.head = None
            self.tail = None
            return node
        
        # Pointers
        position: int = 0
        # Grab the head of the linked list
        current: DoublyNode = self.head
        temp: DoublyNode = self.head.next

        # Loop over the index
        while position < index - 1:
            position += 1
            current = temp
            temp = temp.next
        
        # Remove link
        current.next = temp.next
        # assign current to next node's next previous if exists
        if temp.next:
            temp.next.previous = current
        temp.next = None
        temp.previous = None
        # Return the node
        return temp