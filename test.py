import unittest
from lab7 import cable_length


class TestCableRouting(unittest.TestCase):
    def test_standard_graph(self):
        matrix = [
            [0, 2, 0, 1],
            [2, 0, 3, 4],
            [0, 3, 0, 5],
            [1, 4, 5, 0],
        ]
        self.assertEqual(cable_length(matrix), 6)

    def test_single_island(self):
        matrix = [[0]]
        self.assertEqual(cable_length(matrix), 0)

    def test_empty_graph(self):
        matrix = []
        self.assertEqual(cable_length(matrix), 0)

    def test_disconnected_graph(self):
        matrix = [
            [0, 5, 0],
            [5, 0, 0],
            [0, 0, 0],
        ]
        with self.assertRaises(ValueError):
            cable_length(matrix)

    def test_fully_connected_graph(self):
        matrix = [
            [0, 5, 5],
            [5, 0, 5],
            [5, 5, 0],
        ]
        self.assertEqual(cable_length(matrix), 10)


if __name__ == "__main__":
    unittest.main()