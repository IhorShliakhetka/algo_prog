import unittest
from lab5 import flood_fill


class TestFloodFill(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "G", "X", "X", "X"],
            ["G", "G", "G", "G", "G", "G", "G", "X", "X", "X"],
            ["W", "W", "W", "W", "W", "G", "G", "G", "G", "X"],
            ["W", "R", "R", "R", "R", "R", "G", "X", "X", "X"],
            ["W", "W", "W", "R", "R", "G", "G", "X", "X", "X"],
            ["W", "B", "W", "R", "R", "R", "R", "R", "R", "X"],
            ["W", "B", "B", "B", "B", "R", "R", "X", "X", "X"],
            ["W", "B", "B", "X", "B", "B", "B", "B", "X", "X"],
            ["W", "B", "B", "X", "X", "X", "X", "X", "X", "X"],
        ]

    def test_flood_fill_example(self):
        expected_matrix = [
            ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "G", "C", "C", "C"],
            ["G", "G", "G", "G", "G", "G", "G", "C", "C", "C"],
            ["W", "W", "W", "W", "W", "G", "G", "G", "G", "C"],
            ["W", "R", "R", "R", "R", "R", "G", "C", "C", "C"],
            ["W", "W", "W", "R", "R", "G", "G", "C", "C", "C"],
            ["W", "B", "W", "R", "R", "R", "R", "R", "R", "C"],
            ["W", "B", "B", "B", "B", "R", "R", "C", "C", "C"],
            ["W", "B", "B", "C", "B", "B", "B", "B", "C", "C"],
            ["W", "B", "B", "C", "C", "C", "C", "C", "C", "C"],
        ]
        
        result = flood_fill(self.matrix, 3, 9, "C")
        self.assertEqual(result, expected_matrix)

    def test_same_color(self):
        small_matrix = [["X", "X"], ["X", "X"]]
        result = flood_fill(small_matrix, 0, 0, "X")
        self.assertEqual(result, [["X", "X"], ["X", "X"]])

    def test_out_of_bounds(self):
        with self.assertRaises(IndexError):
            flood_fill(self.matrix, 15, 15, "C")

    def test_empty_matrix(self):
        self.assertEqual(flood_fill([], 0, 0, "C"), [])


if __name__ == "__main__":
    unittest.main()