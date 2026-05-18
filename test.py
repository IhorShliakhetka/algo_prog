import unittest
from lab8 import solve_ijones


class TestIJones(unittest.TestCase):
    def test_example_1(self):
        w, h = 3, 3
        grid = [
            "aaa", 
            "cab", 
            "def"
        ]
        self.assertEqual(solve_ijones(w, h, grid), 5)

    def test_example_2(self):
        w, h = 10, 1
        grid = [
            "abcdefaghi"
        ]
        self.assertEqual(solve_ijones(w, h, grid), 2)

    def test_example_3(self):
        w, h = 7, 6
        grid = [
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa"
        ]
        self.assertEqual(solve_ijones(w, h, grid), 201684)

if __name__ == "__main__":
    unittest.main()