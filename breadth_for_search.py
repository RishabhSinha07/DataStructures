class newNode:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.key = data


def printLevelOrder(node):
    temp = node
    q = [temp]

    while len(q) > 0 :
        print(q[0].key)
        node = q.pop(0)

        if node.left is not None:
            q.append(node.left)

        if node.right is not None:
            q.append(node.right)


if __name__ == "__main__":
    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(15)
    root.right.right = newNode(8)
    printLevelOrder(root)
