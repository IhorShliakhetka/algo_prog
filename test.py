import unittest

from lab4 import AVLPriorityQueue


class TestAVLPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = AVLPriorityQueue()

    def test_empty_queue_pop_raises_error(self):
        with self.assertRaises(IndexError):
            self.pq.pop()

    def test_empty_queue_peek_returns_none(self):
        self.assertIsNone(self.pq.peek())

    def test_insert_and_peek(self):
        self.pq.insert("Low priority", 1)
        self.pq.insert("High priority", 10)
        self.pq.insert("Medium priority", 5)

        self.assertEqual(self.pq.peek(), ("High priority", 10))

    def test_pop_order(self):
        self.pq.insert("Task 1", 5)
        self.pq.insert("Task 2", 15)
        self.pq.insert("Task 3", 1)
        self.pq.insert("Task 4", 8)

        self.assertEqual(self.pq.pop(), ("Task 2", 15))
        self.assertEqual(self.pq.pop(), ("Task 4", 8))
        self.assertEqual(self.pq.pop(), ("Task 1", 5))
        self.assertEqual(self.pq.pop(), ("Task 3", 1))

    def test_same_priority(self):
        self.pq.insert("A", 5)
        self.pq.insert("B", 5)
        self.pq.insert("C", 5)

        _, prio1 = self.pq.pop()
        _, prio2 = self.pq.pop()
        _, prio3 = self.pq.pop()

        self.assertEqual(prio1, 5)
        self.assertEqual(prio2, 5)
        self.assertEqual(prio3, 5)

    def test_avl_balance(self):
        for i in range(1, 20):
            self.pq.insert(f"Task {i}", i)

        def check_balance_and_height(node):
            if not node:
                return 0

            left_height = check_balance_and_height(node.left)
            right_height = check_balance_and_height(node.right)

            self.assertTrue(
                abs(left_height - right_height) <= 1,
                f"AVL-дерево розбалансоване у вузлі {node.priority}",
            )

            return 1 + max(left_height, right_height)

        check_balance_and_height(self.pq.root)


if __name__ == "__main__":
    unittest.main()