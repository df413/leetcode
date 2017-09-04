# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:  
            return t2

        if not t2:
            return t1

        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t2.right = self.mergeTrees(t1.right, t2.right)

        return t1


if __name__ == "__main__":
    # building a tree
    tree1 = TreeNode(1)
    ch = TreeNode(3)
    ch.left = TreeNode(5)
    tree1.left = ch


