class Solution(object):
    def qsort(self, arr):
        """
        O(n log(n)); space: log(n)
        :param arr:
        :return:
        """
        print(arr)
        if len(arr) <= 1:
            return arr
        else:
            return self.qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + \
                    self.qsort([x for x in arr[1:] if x >= arr[0]])

    def my_quicksort(self, myList, start, end):
        if start < end:
            # partition the list
            pivot = self.partition(myList, start, end)
            # sort both halves
            self.my_quicksort(myList, start, pivot - 1)
            self.my_quicksort(myList, pivot + 1, end)
        return myList

    def partition(self, myList, start, end):
        pivot = myList[start]
        left = start + 1
        right = end
        done = False

        while not done:
            while left <= right and myList[left] <= pivot:
                left = left + 1

            while myList[right] >= pivot and right >= left:
                right = right - 1

            if right < left:
                done = True
            else:
                # swap places
                temp = myList[left]
                myList[left] = myList[right]
                myList[right] = temp

        # swap start with myList[right]
        temp = myList[start]
        myList[start] = myList[right]
        myList[right] = temp
        return right


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 10, -1, 0, 5]
    sol.my_quicksort(arr, 0, len(arr)-1)
    print(arr)
