class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.key = data

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def dia(node):

    if node is None:
        return 0

    lheight = height(node.left)
    rheight = height(node.right)

    ldiameter = dia(node.left)
    rdiameter = dia(node.right)

    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print('Height of the tree is: ',height(root))
    print('Diameter of the tree is: ',dia(root))

if __name__ == "__main__":
    main()