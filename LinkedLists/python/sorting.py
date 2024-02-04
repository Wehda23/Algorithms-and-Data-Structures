"""
This File contains Interface Classes
"""
from abc import ABC, abstractmethod


class LinkedListSorting(ABC):
    @abstractmethod
    def sort(self):
        pass

class MergeSorter(LinkedListSorting):
    pass

class InsertSort(LinkedListSorting):
    pass

class BubbleSort(LinkedListSorting):
    pass

class SelectionSort(LinkedListSorting):
    pass

class ShellSort(LinkedListSorting):
    pass
