"""
This file is to test our Node Class to make sure everything is working properly.

Unittest for Class:
Class Node
Class DoublyNode
"""

import unittest
from nodes import Node, DoublyNode


class TestNode(unittest.TestCase):
    """
    Unittest Class for Class Node
    """

    def test_initialize_node(self):
        node: Node = Node(5)
        self.assertEqual(node.value, 5)
        self.assertIsNone(node.next)

    def test_set_next_node(self):
        node1: Node = Node(1)
        node2: Node = Node(2)
        node1.next: Node = node2
        self.assertEqual(node1.next, node2)

    def test_validate_value(self):
        with self.assertRaises(TypeError):
            node: Node = Node("test")

    def test_validate_node(self):
        node1: Node = Node(1)
        node2: str = "test"
        with self.assertRaises(TypeError):
            node1.next: Node = node2


class TestDoublyNode(unittest.TestCase):
    """
    Unittest Class for Class DoublyNode
    """

    def test_initialize_node(self):
        node: DoublyNode = DoublyNode(5)
        self.assertEqual(node.value, 5)
        self.assertIsNone(node.previous)
        self.assertIsNone(node.next)

    def test_set_next_node(self):
        node1: DoublyNode = DoublyNode(10)
        node2: DoublyNode = DoublyNode(15)
        node1.next = node2
        self.assertEqual(node1.next, node2)

    def test_set_previous_node(self):
        node1: DoublyNode = DoublyNode(10)
        node2: DoublyNode = DoublyNode(15)
        node1.previous = node2
        self.assertEqual(node1.previous, node2)

    def test_validate_value(self):
        with self.assertRaises(TypeError):
            node: DoublyNode = DoublyNode("test")

    def test_validate_node(self):
        node1: DoublyNode = DoublyNode(1)
        node2: str = "test"
        with self.assertRaises(TypeError):
            node1.next: DoublyNode = node2


if __name__ == "__main__":
    unittest.main()
