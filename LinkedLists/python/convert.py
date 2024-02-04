"""
This File contains interface classes used to convert linked list to other types of Data Structures
"""
from abc import ABC, abstractmethod



class ConvertLinkedList(ABC):
    """
    Abstracted Class
    """
    @abstractmethod
    def to(self):
        pass

class LinkedListToList(ConvertLinkedList):
    pass

class LinkedListToDict(ConvertLinkedList):
    pass

class LinkedListToSet(ConvertLinkedList):
    pass