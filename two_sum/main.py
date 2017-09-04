class Solution(object):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """
    def twoSum(self, nums: list, target: int)-> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m_dict = dict()
        out_list = list()

        for i in range(0, len(nums)):
            if nums[i] in m_dict:
                out_list.append(m_dict.get(nums[i]))
                out_list.append(i)
                break
            else:
                m_dict[target - nums[i]] = i

        return out_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(nums=[2, 7, 11, 15], target=9))

