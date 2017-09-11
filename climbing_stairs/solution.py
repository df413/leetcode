

class Solution(object):
    """
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
    def calculate_climbing_stairs(self, n):
        """
        :param n:
        :return: int: number of ways
        Let's use fibonacci pattern
        """
        first = 1
        second = 2

        if n < 3:
            return n

        for i in range(3, n + 1):
            first, second = second, first + second

        return second

if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate_climbing_stairs(3))
