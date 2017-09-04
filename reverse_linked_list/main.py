class Node(object):
    def __init__(self):
        self.val = None
        self.next = None


class Solution(object):
    def reverse_linked_list(self, head: Node):
        prev = None
        current = head

        while current:
            next_item = current.next
            current.next = prev
            prev = current
            current = next_item

        return prev

    def print_linked_list(self, obj: Node):
        i = 0
        while obj:
            print("{}: {}".format(i, obj.val))
            obj = obj.next
            i += 1


if __name__ == "__main__":
    sol = Solution()
    n = Node(); n.val = 1
    n1 = Node(); n1.val = 2
    n2 = Node(); n2.val = 3
    n3 = Node(); n3.val = 4

    n.next = n1
    n1.next = n2
    n2.next = n3

    ob = sol.reverse_linked_list(n)
    sol.print_linked_list(ob)