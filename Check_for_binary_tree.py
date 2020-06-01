temp = []

def check_binary_search_tree_(root):
    if root.left:
        check_binary_search_tree_(root.left)
    if root:
        temp.append(root.data)
    if root.right:
        check_binary_search_tree_(root.right)

    for val in range(len(temp) - 1):
        if temp[val] < temp[val + 1]:
            continue
        else:
            return False
    return True
