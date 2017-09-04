class Solution(object):
    def __init__(self):
        self.index_0 = 0
        self.index_1 = 1

    def fib(self, n: int) -> iter:
        yield self.index_0
        yield self.index_1

        for i in range(2, n+1):
            self.index_0, self.index_1 = self.index_1, self.index_0 + self.index_1
            yield self.index_1

if __name__ == "__main__":
    sol = Solution()
    for fib_number in sol.fib(10):
        print("{}, ".format(fib_number))
