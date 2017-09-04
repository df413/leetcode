class Solution(object):
    """
    Remove duplicates in 0(1) space complexity
    """
    def find_all_duplicates_in_O_from_1_space_complexity(self, l):
        for i in range(len(l)):
            if l[abs(l[i])] >= 0:
                l[abs(l[i])] = - l[abs(l[i])]
            else:
                print(abs(l[i]))

    def find_duplicates_another_solution(self, l):
        l.sort()

        for i in range(len(l) - 2):
            if l[i] == l[i+1]:
                print(l[i])

if __name__ == "__main__":
    """
    """
    sol = Solution()
    sol.find_duplicates_another_solution([8, 2, 3, 6, 2, 4, 10, 6, 9, 9, 1, 9, 1])
