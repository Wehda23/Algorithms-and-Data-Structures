import unittest
from nodes import Node

class TestNode(unittest.TestCase):
    def test_initialize_node(self):
        node = Node(5)
        self.assertEqual(node.value, 5)
        self.assertIsNone(node.next)
    def test_set_next_node(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        self.assertEqual(node1.next, node2)
    def test_validate_value(self):
        with self.assertRaises(TypeError):
            node = Node('test')
    def test_validate_node(self):
        node1 = Node(1)
        node2 = 'test'
        with self.assertRaises(TypeError):
            node1.next = node2

if __name__ == '__main__':
    unittest.main()