

class Node:

    def __init__(self, prev = None, next = None, data = None):
        self.next = next
        self.prev = prev
        self.data = data


def push(self, new_data):

    new_node = Node(new_data)

    new_node.next = self.head
    new_node.prev = None

    if self.head is not None:
        self.head.prev = new_node

    self.head = new_node


