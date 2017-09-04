class Solution(object):
    """
    Given an array of size n, find the majority element.
    The majority element is the element that appears more than ⌊ n/2 ⌋ times.
    You may assume that the array is non-empty and the majority element always exist in the array.
    """
    def find_majority_element(self, array: list) -> int:
        """
        INPLACE method
        :param array: list
        :return: int
        """
        print("Search criteria is {}".format(len(array) // 2))
        # Sort the array
        array.sort()

        print("Sorted array is {}".format(array))
        delta = 1

        for i in range(len(array) - 1):
            if delta > len(array) // 2:
                print("found element under index {}".format(i))
                return array[i]

            if array[i] == array[i+1]:
                delta += 1
            else:
                delta = 1

    def find_majority_element_memory(self, array: list) -> int:
            majority_map = dict()
            array_len = len(array) // 2
            element = None

            for i in array:
                if i in majority_map:
                    majority_map[i] += 1
                else:
                    majority_map[i] = 1

                if majority_map[i] > array_len:
                    element = i
                    break

            return element

if __name__ == "__main__":
    given_array = [4, 6, 4, 2, 4, 4, 8, 9, 4, 2, 4]
    sol = Solution()
    print(sol.find_majority_element(given_array))
    print(sol.find_majority_element_memory(given_array))
