import unittest
from generate_all_possible_permutations.main import *


class TestPermutation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_swap_function(self):
        a = 10
        b = 24
        self.assertEqual(
            self.solution.swap_elements(a, b), (b, a),
            msg="Checking swapping of elements")


if __name__ == "__main__":
    t = unittest.BaseTestSuite()
    t.addTest(TestPermutation)
    t.run()
