

class Solution(object):
    """
    Given an array of n integers where n > 1, nums,
    return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

    Solve it without division and in O(n).
    For example, given [1,2,3,4], return [24,12,8,6].

    Follow up:
    Could you solve it with constant space complexity?
    (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
    """
    def find_product_division(self, l):
        out_list = []
        acc = 1

        # with division first
        for i in l:
            acc *= i

        for i in l:
            out_list.append(acc // i)

        return out_list

    def find_product(self, l):
        out_list = []
        acc = 1
        # with division first
        for i in l:
            acc *= i

        for i in l:
            out_list.append(acc // i)

        return out_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.find_product([1, 2, 3, 4]))
