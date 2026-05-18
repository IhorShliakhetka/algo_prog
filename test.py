import unittest
from lab9 import finite_automaton_search


class TestFSMSearch(unittest.TestCase):
    def test_basic_search(self):
        haystack = "AABAACAADAABAABA"
        needle = "AABA"
        expected = [0, 9, 12]
        self.assertEqual(finite_automaton_search(haystack, needle), expected)

    def test_no_match(self):
        haystack = "THIS IS A SIMPLE TEXT"
        needle = "COMPLEX"
        expected = []
        self.assertEqual(finite_automaton_search(haystack, needle), expected)

    def test_overlapping_matches(self):
        haystack = "AAAAA"
        needle = "AA"
        expected = [0, 1, 2, 3]
        self.assertEqual(finite_automaton_search(haystack, needle), expected)

    def test_empty_needle(self):
        haystack = "HELLO WORLD"
        needle = ""
        expected = []
        self.assertEqual(finite_automaton_search(haystack, needle), expected)

if __name__ == "__main__":
    unittest.main()