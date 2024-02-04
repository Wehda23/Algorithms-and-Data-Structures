"""
This File contains interface classes used to convert linked list to other types of Data Structures
"""
from abc import ABC, abstractmethod



class ConvertLinkedList(ABC):
    """
    Interface Class
    """
    @abstractmethod
    def convert(self):
        pass

class LinkedListToList(ConvertLinkedList):
    pass

class LinkedListToDict(ConvertLinkedList):
    pass

class LinkedListToSet(ConvertLinkedList):
    pass