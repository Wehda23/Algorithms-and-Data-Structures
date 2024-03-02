"""
File that contains linkedlist node validators
"""
from abc import ABC, abstractmethod
from typing import NoReturn, Union


class AbstractNodeValidator(ABC):
    """
    Abstract Class showing the LinkedList Node Validator
    """

    @abstractmethod
    def validate_node(self, node: object) -> Union[None, NoReturn]:
        pass
