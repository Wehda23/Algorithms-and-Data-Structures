"""
File that contains linkedlistiterators
"""

class LinkedListIterator:
    """
    Class used as a helper to iterate over a linked list
    """

    def __init__(self, head: object):
        """
        Initializes an iterator object with the given node.

        Args:
            - head: Pointer to the head of the node
        """

        self.current: object = head

    def __iter__(self) -> object:
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