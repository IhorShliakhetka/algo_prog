import unittest

from lab3 import BinaryTree, find_successor


class TestTreeBeginner(unittest.TestCase):
    def test_1(self):
        #        3
        #       /  \
        #      9    20
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)

        successor = find_successor(root, root.left)
        self.assertEqual(successor, root)
        self.assertEqual(successor.value, 3)

    def test_2(self):
        #        10
        #       /  \
        #      5    15
        #     / \     \
        #    3   7     20
        #             /
        #            12
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(15)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.right.right = BinaryTree(20)
        root.right.right.left = BinaryTree(12)

        target_node = root.left.right
        
        successor = find_successor(root, target_node)
        
        self.assertEqual(successor, root)
        self.assertEqual(successor.value, 10)


if __name__ == "__main__":
    unittest.main()