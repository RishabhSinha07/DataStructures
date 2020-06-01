class Node:

    def __init__(self,left = None, right = None, data = None):
        self.left = left
        self.right = right
        self.val = data

def inorder(root):
    if root:
        print("dsa")
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def __main__():
    print("im")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    inorder(root)