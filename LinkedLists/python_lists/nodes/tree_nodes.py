"""
File that contains Nodes that are created for tree data structures
"""

from .abstracted_node import (
    AbstractedRightNode,
    AbstractedLeftNode,
    AbstractedParentNode,
)
from .node_validators import NodeValidator
from typing import Union, Self


class TreeNode(
    AbstractedRightNode, AbstractedLeftNode, AbstractedParentNode, NodeValidator
):
    """
    Class Object that represents Nodes to be used in Tree Data Structures.
    """

    def __init__(
        self: Self,
        value: int,
        parent: Union["TreeNode", None] = None,
        right: Union["TreeNode", None] = None,
        left: Union["TreeNode", None] = None,
    ) -> None:
        """
        Initializes a new instance of the TreeNode
        """
        self.value: int = value
        self.parent = parent
        self.right = right
        self.left = left

    @property
    def parent(self) -> Union["TreeNode", None]:
        """
        Gets or sets the parent node of this

        Returns:
            - Parent Node or None
        """
        return self._parent

    @parent.setter
    def parent(self, parent: Union["TreeNode", None]) -> None:
        """
        Property Parent Setter to a new value.
        Args:
            - parent (TreeNode | None): TreeNode to set as parent to this Node.

        Raises:
            - TypeError: Incase the parent input object type is different from current class

        Returns:
            - Nothing
        """
        # Only Validate if the parent is not None
        if parent is not None:
            self.validate_node(parent)

        self._parent: Union["TreeNode", None] = parent

    @property
    def right(self) -> Union["TreeNode", None]:
        """
        Gets or sets the right node of this

        Returns:
            - right Node or None
        """
        return self._right

    @right.setter
    def right(self, right: Union["TreeNode", None]) -> None:
        """
        Property right Setter to a new value.
        Args:
            - right (TreeNode | None): TreeNode to set as right to this Node.

        Raises:
            - TypeError: Incase the right input object type is different from current class

        Returns:
            - Nothing
        """
        # Only Validate if the right is not None
        if right is not None:
            self.validate_node(right)

        self._right: Union["TreeNode", None] = right

    @property
    def left(self) -> Union["TreeNode", None]:
        """
        Gets or sets the left node of this

        Returns:
            - left Node or None
        """
        return self._left

    @left.setter
    def left(self, left: Union["TreeNode", None]) -> None:
        """
        Property left Setter to a new value.
        Args:
            - left (TreeNode | None): TreeNode to set as left to this Node.

        Raises:
            - TypeError: Incase the left input object type is different from current class

        Returns:
            - Nothing
        """
        # Only Validate if the left is not None
        if left is not None:
            self.validate_node(left)

        self._left: Union["TreeNode", None] = left

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
            raise TypeError("value: Should be of type integer <int>.")

    @property
    def value(self: Self) -> int:
        """
        Property Getter method to get the value of node

        Returns:
            - Integer value of the TreeNode
        """
        return self._value

    @value.setter
    def value(self: Self, value: int) -> None:
        """
        Property Setter method to set new value to the node

        Args:
            - value (int): Integer value to set to the node.

        Raises:
            - TypeError: Incase the value input was not an integer.

        Returns:
            - Nothing.
        """
        # Validate value
        self.validate_value(value)
        self._value: int = value
