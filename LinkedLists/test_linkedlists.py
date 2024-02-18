from python_lists.nodes.nodes import Node, DoublyNode
from python_lists.linked_lists.linkedlists import LinkedList, DoublyLinkedList

node: Node = Node(10)
node2: Node = Node(15)
new_list: LinkedList = LinkedList(10)
new_list.add(node)
new_list.add(node2)
node3: Node = new_list.create_node(22)
new_list.add(node3)

print(new_list)
copy_list: list = new_list.to_list()
copy_set: set = new_list.to_set()

print(type(copy_list), " ", copy_list)
print(type(copy_set), " ", copy_set)
print(type(copy_list[0]))
print(len(new_list))
print(repr(new_list))
