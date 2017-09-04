class Solution(object):
    def reverse_integer(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False

        if x < 0:
            flag = True
            x = abs(x)

        res = 0
        max_int = 2 ** 31 - 1

        while x:
            temp = res * 10 + x % 10
            if temp // 10 != res:
                return 0

            res = temp
            x = x // 10

        if res > max_int:
            return 0

        return res if not flag else -res


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse_integer(123))
