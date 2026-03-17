class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    nodes_list = []

    def traverse(current):
        if current is not None:
            traverse(current.left)
            nodes_list.append(current)
            traverse(current.right)

    traverse(tree)
    
    for i in range(len(nodes_list)):
        if nodes_list[i] == node:
            if i + 1 < len(nodes_list):
                return nodes_list[i + 1]
    return None