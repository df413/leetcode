

class Solution(object):
    def merge_two_sorted_arrays(self, arr1, arr2):
        arr1_tail = len(arr1) - len(arr2) - 1
        arr2_tail = len(arr2) - 1

        for counter in range(len(arr1) - 1, -1, -1):
            if arr1_tail == -1:
                arr1[counter] = arr2[arr2_tail]
                arr2_tail -= 1

            elif arr2_tail == -1:
                arr1[counter] = arr1[arr1_tail]
                arr1_tail -= 1

            else:
                if arr1[arr1_tail] >= arr2[arr2_tail]:
                    arr1[counter] = arr1[arr1_tail]
                    arr1_tail -= 1
                else:
                    arr1[counter] = arr2[arr2_tail]
                    arr2_tail -= 1


if __name__ == "__main__":
    arr_1 = [13, 18, 0, 0, 0]
    arr_2 = [2, 7, 9]

    sol = Solution()
    sol.merge_two_sorted_arrays(arr_1, arr_2)

    print(arr_1)
