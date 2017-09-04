class Solution(object):
    def find_all_ones(self, number: int) -> int:
        res = 0
        mask = 1

        print("bin repr of number {} is {}".format(number, bin(number)))

        while mask <= number:
            if number & mask > 0:
                res += 1

            mask = mask << 1

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.find_all_ones(12))
