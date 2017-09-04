class Solution(object):
    """
    Given a list of Integers. Generate all possible permutations
    """
    def permutation(self, input_list):
        if len(input_list) == 2:
            yield [input_list[0], input_list[1]]
            yield [input_list[1], input_list[0]]
        else:
            for element in input_list:
                # copying list to sub_list
                sub_list = input_list[:]
                sub_list.remove(element)

                for processed_list in self.permutation(sub_list):
                    processed_list.insert(0, element)
                    yield processed_list

    def swap_elements(self, a, b):
        a ^= b
        b ^= a
        a ^= b
        return a, b

    def heap_permutation(self, array: list, array_size: int):
        if array_size == 1:
            print(array)
            return

        for i in range(array_size):
            self.heap_permutation(array, array_size-1)
            # if the size is odd
            if array_size % 2 == 1:
                array[0], array[array_size-1] = self.swap_elements(array[0], array[array_size-1])
            else:
                array[i], array[array_size - 1] = self.swap_elements(array[i], array[array_size - 1])

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2]

    sol.heap_permutation(arr, len(arr))

