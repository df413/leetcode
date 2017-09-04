

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

    def print_linked_list(self, obj: Node):
        i = 1
        while obj:
            print("{}: {}".format(i, obj.val))
            obj = obj.next
            i += 1

    def removeNthFromEnd(self, head, n):
        # the idea is like sliding window...
        """
        :param head:
        :param n:
        :return:
        """
        head_pointer = head
        prev_head_pointer = head
        tail_pointer = head

        current_node = head
        counter = 1

        while current_node:

            if counter <= n:
                tail_pointer = current_node
            else:
                prev_head_pointer = head_pointer
                head_pointer = head_pointer.next
                tail_pointer = tail_pointer.next

            counter += 1
            current_node = current_node.next

        if head == head_pointer:
            head = head_pointer.next

        else:
            # deleting element from linked_list
            prev_head_pointer.next = head_pointer.next

        return head

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)  # this should disappear
    head.next.next.next.next = Node(5)

    sol = Solution()

    sol.print_linked_list(sol.removeNthFromEnd(head, 5))
