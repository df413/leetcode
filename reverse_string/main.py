
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = bytearray(s, "utf8")
        arr.reverse()

        return arr.decode("utf8")

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseString("hello"))
