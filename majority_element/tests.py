import unittest
from majority_element.solution import Solution


class TestSetForMajorityElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_array_with_size_1(self):
        test_array = [1]

        self.assertEqual(self.solution.find_majority_element(test_array), None)

    def test_array_with_size_2(self):
        test_array = [1, 2]

        self.assertEqual(self.solution.find_majority_element(test_array), None)

    def test_array_with_size_3(self):
        test_array = [1, 2, 2]

        self.assertEqual(self.solution.find_majority_element(test_array), None)

    def test_array_with_size_4(self):
        test_array = [1, 1, 1, 2]

        self.assertEqual(self.solution.find_majority_element(test_array), 1)

    def test_array_with_all_zeroes(self):
        test_array = [0] * 10

        self.assertEqual(self.solution.find_majority_element(test_array), 0)

    def test_array_with_empty_array(self):
        test_array = []

        self.assertEqual(self.solution.find_majority_element(test_array), None)

    def test_array_with_negative_numbers(self):
        test_array = [-50, -5, -50, -50, -2, -8, -50, -50, -1, -50, -50]

        self.assertEqual(self.solution.find_majority_element(test_array), -50)

    def test_big_array(self):
        test_array = [2147483647] * 21474 + [2, 9, 11, 15] * 3

        self.assertEqual(self.solution.find_majority_element(test_array), 2147483647)


if __name__ == "__main__":
    unittest.main()
