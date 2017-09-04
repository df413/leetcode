

class Node(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __repr__(self):
        next_item = self

        while next_item:
            print(next_item.val)
            next_item = next_item.next

        return ""


class Solution(object):
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    4+3 = 7
    6 + 4 = 0
    2 + 5 = 7 or 8 because prev was 10 so 7 + 1...
    """
    def add_two_numbers(self, l1, l2):

        current_l1 = l1
        current_l2 = l2

        dummyNode = None
        extra = 0

        while current_l1 and current_l2:
            current_sum = current_l1.val + current_l2.val + extra
            extra = current_sum / 10

            dummyNode.next = Node(current_sum % 10)
            dummyNode = dummyNode.next

            current_l1 = current_l1.next
            current_l2 = current_l2.next

        if extra > 0:
            dummyNode.next = Node(extra)

        return dummyNode.next

if __name__ == "__main__":
    n1 = Node()
    n1.val = 2
    n2 = Node()
    n2.val = 4
    n3 = Node()
    n3.val = 3

    n1.next = n2
    n2.next = n3

    m1 = Node()
    m1.val = 5
    m2 = Node()
    m2.val = 6
    m3 = Node()
    m3.val = 4

    m1.next = m2
    m2.next = m3
    # n1 = Node()
    # n1.val = 5
    #
    #
    # m1 = Node()
    # m1.val = 5

    print(m1)
    print(n1)

    sol = Solution()
    print(sol.add_two_numbers(n1, m1))

