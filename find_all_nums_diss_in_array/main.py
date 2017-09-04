class Solution(object):
    """
    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
    some elements appear twice and others appear once.
    Find all the elements of [1, n] inclusive that do not appear in this array.
    Could you do it without extra space and in O(n) runtime?
    You may assume the returned list does not count as extra space.

    Input:
        [4,3,2,7,8,2,3,1]
    Output:
        [5,6]
    """
    def find_all_nums_diss_in_array(self, nums):
        missing_num_list = list()

        for i in range(len(nums)):
            if nums[abs(nums[i])-1] >= 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

        for num in nums:
            if num > 0:
                missing_num_list.append(nums.index(num) + 1)
        return missing_num_list

if __name__ == "__main__":
    sol = Solution()
    print(sol.find_all_nums_diss_in_array([4, 3, 2, 7, 8, 2, 3, 1]))
