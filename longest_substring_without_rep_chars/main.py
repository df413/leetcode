class Solution(object):
    """
    Given a string, find the length of the longest substring without repeating characters.
    Examples:
        Given "abcabcbb", the answer is "abc", which the length is 3.
        Given "bbbbb", the answer is "b", with the length of 1.
        Given "pwwkew", the answer is "wke", with the length of 3.
        Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = dict()

        n = len(s)
        i = 0
        j = 0
        res = 0

        while j < n:
            if s[j] in char_map:
                i = max(char_map.get(s[j]), i)

            res = max(res, j - i + 1)
            char_map[s[j]] = j + 1

            # incrementing j
            j += 1

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s="abcabcbb"))
    print(sol.lengthOfLongestSubstring(s="bbbbb"))
    print(sol.lengthOfLongestSubstring(s="pwwkew"))
