from typing import Union
"""
This File contains class to create nodes in Python

Contains the following classes:

Class Node (Represents Singly Linked Nodes that travers only forward.)
Class DoublyNode (Represents a Doubly Linked Nodes that can traverse both directions <Backwards, Forwards>).
"""



class Node:
    """
    Base Class for creating nodes in python
    
    Singly linked List Nodes

    Traverse only Forward
    """
    def __init__(self, value: int, next: Union["Node", None] = None):
        """
        Initializes a new instance of the Node class.

        Args:
            - value (int): Integer value stored in the node.
            - next  (<Node> | None): points to the next object of the same class type (default: None).
        """
        # set value
        self.value: int = value
        
        self.next: "Node" | None = next
    
    # Representations
    def __repr__(self) -> str:
        """
        Method used to return a representation of the class

        Returns:
            - Class(parameter, ...)
        """
        return "{}({}, {})".format(
            self.__class__.__name__,
            self.value,
            self.next,
        )
    
    def __str__(self) -> str:
        """
        Method used to return Str representation of the class

        Returns:
            - Python String.
        """
        return "{}({})".format(self.__class__.__name__, self.value)
    
    # Encapsulation
    @property
    def next(self) -> Union["Node", None]:
        """
        Property method used to return next value

        Returns:
            - False in case if next node does not exists otherwise next Node of Type <Node>
        """
        return self._next
    
    @next.setter
    def next(self, new_node: Union["Node", None]) -> None:
        """
        Property Setter Method used to set the new node of type <Node>

        Raises: TypeError incase if the type does not match <Node>

        Args:
            - new_node (<Node> | None): Should be of type <Node>

        Returns:
            - Nothing
        """
        # Only Validate if the new_node is not None
        if new_node is not None:
            self.validate_node(new_node)

        self._next: "Node" | None = new_node
    
    def validate_node(self, node) -> None:
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
            raise ValueError(f"node: Should be of type {self.__class__.__name__}.")
        
    @property
    def value(self) -> int:
        """
        Property method to return value

        Returns:
            - value of the node as integer.
        """
        return self._value
    
    @value.setter
    def value(self, new_value: int) -> None:
        """
        Property Setter method to set a new value to node's value.

        Args:
            - value (int): Integer value to set for node
        
        Returns:
            - Nothing
        """
        # Validate value 
        self.validate_value(new_value)
        self._value: int = new_value

    def validate_value(self, value: int) -> None:
        """
        Class Method used to validate the value will raise error incase of failure

        Args:
            - value (int): integer value

        Raises: TypeError incase of error

        Returns:
            - Nothing
        """
        # Check type of value
        if not isinstance(value, int):
            raise ValueError("value: Should be of type integer <int>.")
        

class DoublyNode(Node):
    """
    Class for creating Doubly linked nodes in python
    
    Doubly linked List Nodes

    Traverse Backwards & Forwards
    """
    
    def __init__(self, value: int, previous: Union["DoublyNode" , None] = None, next: Union["DoublyNode" , None] = None):
        """
        Initializes a new instance of the Node class.

        Args:
            - value (int): integer value
            - previous (<DoublyNode> | None): points to the previous object of the same class type (default: None).
            - next (<DoublyNode> | None): points to the next object of the same class type (default: None).
        """
        super().__init__(value, next)

        self.previous: "DoublyNode" | None = previous

    @property
    def previous(self) -> Union["DoublyNode" , None]:
        """
        Property Method used to returns previous DoublyNode/None
        
        Returns:
            - This Node self.previous or None incase of does not exist
        """
        return self._previous
    
    @previous.setter
    def previous(self, new_previous: Union["DoublyNode" , None]) -> None:
        """
        Setter method for setting the previous property

        Args:
            - new_previous (<DoublyNode> | None): Adds value to self.previous node.
        
        Raises: incase of type difference raises TypeError.
            
        Returns:
            - Nothing.
        """

        # Only Validate if the new_previous is not None
        if new_previous is not None:
            self.validate_node(new_previous)

        self._previous: "DoublyNode" | None = new_previous